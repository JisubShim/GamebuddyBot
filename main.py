import discord, asyncio, random, time, os
from discord.ext import commands
from openai import OpenAI
import requests
from bs4 import BeautifulSoup
from crawling import get_steam_games
from openai_func import create_thread_message, check_run_status, initialize_thread, recreate_assistant
from keep_alive import keep_alive
from help import send_help_message

# 디스코드 봇 intent 설정
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# 파일 예외처리는 꼼꼼하게 작성했습니다.
try:
    with open("token.txt", "r") as file:
        lines = file.readlines()

        if len(lines) < 4:
            raise ValueError("token.txt 파일에 필요한 모든 행이 포함되어 있지 않습니다.")

        TOKEN = lines[0].strip()  # 첫 번째 줄 (Discord 토큰)
        OPENAI_API_KEY = lines[1].strip()  # 두 번째 줄 (OpenAI API 키)
        assistant_id = lines[2].strip()  # 세 번째 줄 (Assistant ID)
        thread_id = lines[3].strip()  # 네 번째 줄 (Thread ID)
except FileNotFoundError:
    print("token.txt 파일을 찾을 수 없습니다. 파일이 올바른 경로에 있는지 확인해주세요.")
except ValueError as e:
    print(f"파일 읽기 오류: {e}")
except Exception as e:
    print(f"예상치 못한 오류가 발생했습니다: {e}")

#replit 배포를 할 때 token을 secret하기 위해 사용
# TOKEN = os.environ['TOKEN']
# OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
# assistant_id = os.environ['ASSISTANT_ID']
# thread_id = os.environ['THREAD_ID']

prefix = '!' # 명령어 접두사 설정

# 디스코드 클라이언트 객체 생성
client = discord.Client(intents=intents)

# OpenAI 클라이언트 객체 생성
ai_client = OpenAI(
    api_key = OPENAI_API_KEY
)

def find_first_channel(channels):
    position_array = [i.position for i in channels]

    for i in channels:
        if i.position == min(position_array):
            return i

@client.event # 데코레이터
async def on_ready(): # 비동기로 함수 선언
    print("반가워 친구!")
    await client.change_presence(status = discord.Status.online, activity = discord.Game('"!도움"으로 나를 불러달라고')) # 상태메세지 설정
    #keep_alive() # replit에 배포 (24시간 구동)
    print('keep_alive() started')

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('안녕 안녕~ 만나서 반가워! 우리 앞으로 잘지내보자!!')
            await channel.send(embed=send_help_message())
            break

  
@client.event
async def on_message(message):
    if message.author.bot: return # 메세지 보낸 사람이 봇이면 무시
    if str(message.channel.type) != 'text': return # 메세지 채널이 채팅 채널이 아니면 무시
    if not message.content.startswith(prefix): return # 메세지가 prefix로 시작하지 않으면 무시
    
    cmd = message.content.split(prefix)[1].split(' ')[0] # 커맨드 입력
    args = message.content.split(cmd)[1][1:].split(' ') # 커맨드 이후 입력
    
    # 이하 각 명령어에 대한 처리 로직 작성

    if cmd == "안녕":
        mar = ' '.join(args)
        # 사용자의 이름을 포함하여 개인화된 인사
        await message.channel.send(f"반가워,{mar} {message.author.display_name}! 😊")

    elif cmd == "도움":
        await message.channel.send(embed=send_help_message())

    elif cmd == "사다리타기":
        # 사용자의 메시지 파싱
        try:
            people, teams = ' '.join(args).split("/")
            person_list = people.strip().split(" ")
            team_list = teams.strip().split(" ")
            random.shuffle(team_list)
            if len(person_list) != len(team_list): # 사람 수 != 팀 수
                await message.channel.send("사람 수와 팀 수가 같아야해! 다시 시도해줘~")
                return
            # 출력
            await message.channel.send("Ok 확인 했어~ 내가 정해줄게!")
            for i in range(len(person_list)):
                await message.channel.send(f"{person_list[i]} ~~~~> {team_list[i]}")
        except ValueError:
            await message.channel.send("잘못 입력 했어! 양식을 다시 보여줄게~")
            await message.channel.send("예시: !사다리타기 윗줄1 윗줄2 윗줄3 / 아랫줄1 아랫줄2 아랫줄3")

    elif cmd == "투표":
        vote = ' '.join(args).split("/")
        vote_title = vote[0]
        vote_option = vote[1:]

        if not vote_option:
            await message.channel.send("투표 항목을 입력해줘~ 예시: !투표 제목/옵션1/옵션2/옵션3")
            await message.channel.send("(옵션은 최대 9개)")
            return

        if len(vote_option) > 9:
            await message.channel.send("최대 9개까지의 옵션만 지원해ㅠㅠ")
            return

        embed = discord.Embed(title=vote_title, description="아래의 옵션에 투표하면 돼!", color=0x00ff00)
        for i, option in enumerate(vote_option, start=1):
            embed.add_field(name=f"옵션 {i}", value=option, inline=False)

        poll_message = await message.channel.send(embed=embed)
        poll_message_id = poll_message.id

        # 각 옵션에 대해 반응 추가
        emojis = ('1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣')[:len(vote_option)]
        for emoji in emojis:
            await poll_message.add_reaction(emoji)

    elif cmd == "랜덤":
        choice = ' '.join(args).split(" ")
        if len(choice) < 2:
            await message.channel.send("옵션을 입력해야해! 예시: !랜덤 옵션1 옵션2 옵션3")
            return
        choicenum = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenum]
        await message.channel.send('👉 ' + choiceresult + ' 👈')

    elif cmd == '대화':
        global thread_id, assistant_id
        try:
            content = ' '.join(args)
            run_id = await create_thread_message(ai_client, thread_id, assistant_id, content)
            status, run = await check_run_status(ai_client, thread_id, run_id)
            
            if status == "completed":
                thread_messages = ai_client.beta.threads.messages.list(thread_id)
                await message.channel.send(thread_messages.data[0].content[0].text.value)
            else:
                await message.channel.send(f"문제가 발생했어: {status}")

        except Exception as e:
            await message.channel.send(f"대화 생성 중 오류가 발생했어ㅠㅠ: {e}")
            return

    elif cmd == '기억초기화':
        thread_id = await initialize_thread(ai_client, thread_id)
        await message.channel.send("응? 뭐야! 너 나한테 뭔짓을 한거야?!")
        await message.channel.send("어어...")
        await message.channel.send("우리 무슨 얘기 하고 있었더라..?")

    # 필요없는 기능이라고 판단하여 주석처리 해놓았습니다.

    # elif message.content == "?ai초기화":
    #     try:
    #         assistant_id = await recreate_assistant(client, ai_client, assistant_id)
    #         await message.channel.send("private command : 어시스턴트 재생성")
    #     except Exception as e:
    #         await message.channel.send(f"대화ai 초기화 중 오류가 발생했어ㅠㅠ: {e}")
    #         return

    elif message.content.startswith('!신규게임'):
        try:
            URL = 'https://store.steampowered.com/search/results/?query&start=0&count=10&sort_by=Released_DESC&supportedlang=koreana&snr=1_7_7_popularnew_7&filter=popularnew&os=win&infinite=1'
            games_info = get_steam_games(URL, 10)

            await message.channel.send("좋아! 새로 나온 게임 10개를 알려줄게!")
            await message.channel.send("새로 나온 게임들:")
            response = "새로 나온 게임들:\n"
            count=1
            for title, url in games_info.items():
                time.sleep(1)
                await message.channel.send(f"{count}. '{title}'\n{url}\n\n")
                count+=1
            await message.channel.send("어때? 내가 추천하는 새로 나온 게임 10개야!")

        except requests.RequestException as e:
            await message.channel.send(f"HTTP 요청 중 오류가 발생했어: {e}")

        except Exception as e:
            await message.channel.send(f"데이터 처리 중 오류가 발생했어: {e}")

    elif message.content.startswith('!할인게임'):
        try:
            URL = 'https://store.steampowered.com/search/results/?query&start=50&count=50&dynamic_data=&force_infinite=1&supportedlang=koreana&ndl=1&snr=1_7_7_151_7&infinite=1'
            games_info = get_steam_games(URL, 10)

            await message.channel.send("좋아! 할인 중인 게임 10개를 알려줄게!")
            await message.channel.send("할인 중인 게임들:")
            response = "할인 중인 게임들:\n"
            count=1
            for title, url in games_info.items():
                time.sleep(1)
                await message.channel.send(f"{count}. '{title}'\n{url}\n\n")
                count+=1
            await message.channel.send("어때? 내가 추천하는 할인 중인 게임 10개야!")

        except requests.RequestException as e:
            await message.channel.send(f"HTTP 요청 중 오류가 발생했어: {e}")

        except Exception as e:
            await message.channel.send(f"데이터 처리 중 오류가 발생했어: {e}")

client.run(TOKEN) # 봇을 온라인으로 전환