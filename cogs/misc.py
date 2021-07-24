import discord
import discord.ext
from discord.ext import commands
import random

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def searchwikipedia(self, ctx, msg):
        """
        finds the wikipedia article of the provided input
        """
        url: str = f"https://en.wikipedia.org/wiki/{msg}"
        embed = discord.Embed(
            title = "Result",
            description = "**{url}**",
            color = 0x00ff00
        )

    @commands.command()
    async def coinflip(self, ctx):
        """
        emulates a coin toss
        """
        random == random.randint(1,2)
        if random == 1:
            embed = discord.Embed(
                title = "Coinflip",
                description = "**Heads!**",
                color = 0x00ff00

            )
        else:
            embed = discord.Embed(
                title = "coinflip",
                description = "**Tails!**",
                color = 0x00ff00
            )
def setup(bot):
    bot.add_cog(misc(bot))