import discord
from discord.ext import commands, tasks
from test_bot_config import BOT_TOKEN # 토큰값

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name) # 봇의 이름 출력 - python_test_bot
    print(bot.user.id) # 봇의 고유 ID넘버 출력 - 18자리 숫자
    print('------')

@bot.event
async def on_member_join(member): # 유저가 서버에 처음 들어왔을때 발생하는 이벤트
    # member 유저에게 메시지를 보낸다.
    await member.send(f'{member.user}님 환영합니다. 봇을 테스트하는 서버 입니다.')

@bot.command()
async def command(ctx): # 명령어 만들기 - 기본
    pass


@bot.command()
async def ping(ctx): # def [명령어](ctx) ex) !ping -> ping == ping(ctx)
    print('확인용 핑')
    await ctx.send('pong')

@bot.command(name='메뉴')# (name='메뉴') ex) !메뉴 -> 메뉴 == (name='메뉴') (O) / def menu(ctx) (X)
async def menu(ctx):
    pass

@bot.command()
async def 상태(ctx, *, arg): # 메시지가 띄어쓰기로 나눠서 들어오는경우 (arg) -> (*, arg) 변경 [ref 상태메시지1]
    send_message = "{0}봇의 상태 메시지 변경했습니다.\n변경 \
        메시지명은 {1}".format(bot.user.name, arg)
    print('확인용 상태')
    await bot.change_presence(activity=discord.Game(name=arg))
    await ctx.send(send_message)
    
@bot.command(name='메시지삭제') # 1.0 이후 붙일 필요성이 없어졌다. (name='메시지삭제', pass_context=True [ref 컨텍스트1]
async def message_clear(ctx, *, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'총 {amount}개 메시지 삭제 지운 사람 : *{ctx.author.name}*님')
    

bot.run(BOT_TOKEN)



"""
비주얼 스튜디오 터미널 clear
ctrl + shift + p -> Terminal:Clear 클릭
import discord - pip install -U discord
"""

'''
상태메시지 1 : https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html?highlight=ctx%20message
컨텍스트1 : https://discordpy.readthedocs.io/en/latest/migrating.html
메시지 꾸미기 1(마크다운): https://support.discord.com/hc/ko/articles/210298617-%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4-%ED%85%8D%EC%8A%A4%ED%8A%B8-101-%EC%B1%84%ED%8C%85-%EC%84%9C%EC%8B%9D-%EA%B5%B5%EA%B2%8C-%EA%B8%B0%EC%9A%B8%EC%9E%84%EA%BC%B4-%EB%B0%91%EC%A4%84-
'''