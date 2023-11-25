import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
client = discord.Client(intents=intents)
token = "MTE3NzkwMjcxNjM4Nzg1MjM4MQ.GmEQVI.2hDUCj-5qZKh2Tcrk7D2HorLCawhk7G39ujOcE" # 봇 토큰

@client.event # 데코레이터
async def on_ready(): # 비동기로 함수 선언
    print("반가워 친구!")

@client.event
async def on_message(message):
    if message.content == "!안녕":
        await message.channel.send("반가워!")
    elif message.content == "!소개":
        emb = discord.Embed(title="안녕! 나는 GameBuddy야!", description="내가 게임할 때 필요하면 아래와 같이 불러줘!", color=0xFF0000)
        emb.add_field(name="!소개", value="현재 임베드창을 띄웁니다.", inline=True)
        emb.add_field(name="!사다리타기", value="사다리타기 게임을 진행합니다.", inline=True)
        await message.channel.send(embed=emb)

client.run(token) # 봇을 온라인으로 전환해주는 코드 (항상 맨 아래 위치)

