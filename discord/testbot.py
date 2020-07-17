import discord
from discord.ext import commands

BOT_TOKEN = 'token'
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def 핑(ctx):
    await ctx.send('퐁!')

@bot.command(name='메시지삭제') # 1.0 이후 붙일 필요성이 없어졌다. (name='메시지삭제', pass_context=True [ref 컨텍스트1]
async def message_clear(ctx, *, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'총 {amount}개의 메시지를 삭제 했습니다. *{ctx.author.name}*님')

bot.run(BOT_TOKEN)


