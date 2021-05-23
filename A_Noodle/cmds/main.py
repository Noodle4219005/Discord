from Github.A_Noodle.core.classes import Cog_extention
import discord
from discord.ext import commands
from core.classes import Cog_extension

class Main(Cog_extension):
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

def setup(bot):
    bot.add_cog(Main(bot))