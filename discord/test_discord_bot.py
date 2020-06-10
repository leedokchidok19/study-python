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
    print('확인용 메뉴')
    return_embed = vch.HelpCommand()
    await ctx.send(embed=return_embed, tts=False)

@bot.command()
async def command1(ctx):
    pass

@bot.command()
async def 상태(ctx, *args): # https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html?highlight=ctx%20message
    send_message = "{0}봇의 상태 메시지 변경했습니다.\n변경 \
        메시지명은 {1}".format(bot.user.name, args)
    print('확인용 상태')
    await bot.change_presence(activity=discord.Game(name=''.join(args)))
    await ctx.send(send_message)

bot.run(BOT_TOKEN)



"""
비주얼 스튜디오 터미널 clear
ctrl + shift + p -> Terminal:Clear 클릭
discord - pip install -U discord
"""