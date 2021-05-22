import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='[')
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(845722197200601109)
    await channel.send(f"{member}join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(845722197200601109)
    await channel.send(f"{member}leave!")

bot.run('ODQ1NzA1MjY4NTMyODcxMjEw.YKk2aA.dbkQ0ErHhop5aTr67Iiq9783WCI')