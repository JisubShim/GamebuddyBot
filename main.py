import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
client = discord.Client(intents=intents)
f = open('token', 'r')
token = f.readline() # 봇 토큰

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
client.run(token)
# def ladder_game(participants, results):
#     """
#     사다리타기 게임 구현.
#     :param participants: 참가자 목록 (리스트).
#     :param results: 결과 목록 (리스트). 참가자 수와 동일해야 함.
#     :return: 각 참가자에 대한 결과를 담은 딕셔너리.
#     """
#     if len(participants) != len(results):
#         return "참가자 수와 결과 수가 일치하지 않습니다."
#     random.shuffle(results)
#     return dict(zip(participants, results))

# bot = commands.Bot(command_prefix='!')

# @bot.command(name='사다리타기')
# async def ladder(ctx, *args):
#     # args에서 참가자와 결과를 분리하여 처리
#     # 예: "!사다리타기 Alice Bob Charlie Diana 상품1 상품2 상품3 꽝"
#     half = len(args) // 2
#     participants = args[:half]
#     results = args[half:]

#     # 사다리타기 게임 실행
#     game_result = ladder_game(participants, results)
#     await ctx.send(game_result)

# # 봇 토큰으로 봇 실행
# bot.run(token)
 # 봇을 온라인으로 전환해주는 코드 (항상 맨 아래 위치)

