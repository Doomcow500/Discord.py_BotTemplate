import discord
import discord.ext
from discord.ext import commands

class membermanagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """
        allows you to ban someone
        """
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned')
         
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """
        allows you to kick someone out of the server
        """
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked')

def setup(bot):
    bot.add_cog(membermanagement(bot))