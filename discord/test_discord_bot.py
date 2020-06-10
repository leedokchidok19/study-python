import discord
from discord.ext import commands, tasks
from test_bot_config import BOT_TOKEN

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name) # 봇의 이름 출력 - python_test_bot
    print(bot.user.id) # 봇의 고유 ID넘버 출력 - 18자리 숫자
    print('------')

@bot.command()
async def ping(ctx): # def [명령어](ctx) ex) !ping -> ping == ping(ctx)
    print('확인용 핑')
    await ctx.send('pong')

@bot.command(name='메뉴')# (name='메뉴') ex) !메뉴 -> 메뉴 == (name='메뉴') (O) / def menu(ctx) (X)
async def menu(ctx):
    pass

@bot.command()
async def command1(ctx):
    pass

@bot.command()
async def 상태(ctx, *, arg): # https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html?highlight=ctx%20message
    send_message = "{0}봇의 상태 메시지 변경했습니다.\n변경 \
        메시지명은 {1}".format(bot.user.name, arg)
    print('확인용 상태')
    await bot.change_presence(activity=discord.Game(name=arg))
    await ctx.send(send_message)
    
@bot.command(name='메시지삭제')
async def message_clear(ctx, arg):
    amount = int(arg)
    await ctx.message.channel.purge(limit=amount)
    await ctx.send(f'총 {int(arg)}개 메시지 삭제')
    
    
@bot.event
async def on_member_join(member): # 유저가 서버에 처음 들어왔을때 발생하는 이벤트
    # member 유저에게 메시지를 보낸다.
    await member.send(f'{member.user}님 환영합니다. 봇을 테스트하는 서버 입니다.')

bot.run(BOT_TOKEN)



"""
비주얼 스튜디오 터미널 clear
ctrl + shift + p -> Terminal:Clear 클릭
import discord - pip install -U discord
"""