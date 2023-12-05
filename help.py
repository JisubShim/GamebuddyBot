import discord

def send_help_message():
    embed = discord.Embed(title="안녕! 나는 GameBuddy야! 🎮",
                          description="게임할 때 도움이 필요하면, 아래 명령어들로 나를 불러줘!",
                          color=0x0400ff)
    embed.set_thumbnail(url="https://drive.google.com/uc?id=1j0EFLE3MKqKgtwfllLbj5GwetKofquZC")  # 봇 이미지 URL
    embed.add_field(name="명령어 설명", value="!도움", inline=False)
    embed.add_field(name="인사하기", value="!안녕", inline=False)
    embed.add_field(name="사다리타기", value="!사다리타기 윗줄1 윗줄2 윗줄3 / 아랫줄1 아랫줄2 아랫줄3", inline=False)
    embed.add_field(name="투표하기", value="!투표 제목/옵션1/옵션2/옵션3 *옵션은 최대 9개*", inline=False)
    embed.add_field(name="랜덤선택", value="!랜덤 옵션1 옵션2 옵션3", inline=False)
    embed.add_field(name="대화하기", value="!대화 대화내용", inline=False)
    embed.add_field(name="대화 Thread 초기화", value="!기억초기화", inline=False)
    embed.add_field(name="신규 게임 추천(STEAM)", value="!신규게임", inline=False)
    embed.add_field(name="할인 게임 추천(STEAM)", value="!할인게임", inline=False)
    embed.set_footer(text="언제든 불러줘~ 나 심심해~ 뿅!")
    
    return embed