import discord
from discord.ext import commands, tasks
from discord.ext.commands import Cog
import datetime
import random
anon = ["anon", "anonymous user", "someone", "unknown user" ,"iwik?" ,"the old kiwi"]


class Mail(Cog):
    """
    Idiot!
    """

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def anonmail(self, ctx, *, the_text: str):
        """[U] Help me."""
        channel = self.bot.get_channel(1281252582504923207)
        the_text = f"**FROM:" + random.choice(anon) + f"!**\n{the_text}"
        await channel.send(the_text)
        await ctx.message.reply("message sent!.", mention_author=False)
        
    @commands.command()
    async def mail(self, ctx, *, the_text: str):
        """[U] Help me."""
        channel = self.bot.get_channel(1281252582504923207)
        the_text = f"**FROM: {ctx.author.display_name}!**\n{the_text}"
        await channel.send(the_text)
        await ctx.message.reply("message sent!.", mention_author=False)

async def setup(bot):
    await bot.add_cog(Mail(bot))
