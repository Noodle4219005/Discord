from discord.ext.commands.core import command
from Github.A_Noodle.core.classes import Cog_extension
import discord
from discord.ext import commands
import random
import json

with open('settings.json','r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_extension):

    @commands.command()
    async def picture(self.ctx):
        random_pic = random.choice(jdata['pic']) 
        pic = discord.File(random_pic)
        await ctx.send(file= pic)

def setup(bot):
    bot.add_cog(React(bot))