import discord
from discord.ext import commands

class Cog_extension(commands.cog):
    def __int__(self, bot):
        self.bot = bot