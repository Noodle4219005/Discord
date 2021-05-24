import discord
from discord.channel import VocalGuildChannel, VoiceChannel
from discord.ext import commands

import json
import random
import os

with open('settings.json','r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='[', intents=intents)
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['WelcomeChannel']))
    await channel.send(f"{member}join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['RemoveChannel']))
    await channel.send(f"{member}leave!")
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def picture(ctx):
    random_pic = random.choice(jdata['pic']) 
    pic = discord.File(random_pic)
    await ctx.send(file= pic)

@bot.command()
async def Kevin(ctx):
    await ctx.send('陳冠綸是白癡')

@bot.command()
async def Evan(ctx):
    await ctx.send('李翊綸噁男')

@bot.command()
async def play(ctx, url : str):
    VocalChannel = discord.utils.get(ctx.guild.voice_channels, name = '一般')

bot.run(jdata['TOKEN'])