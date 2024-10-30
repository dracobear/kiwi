import discord
from discord.ext import commands, tasks
from discord.ext.commands import Cog
import datetime
import random
from helpers.checks import ismanager
anon = ["anon", "anonymous user", "someone", "unknown user" ,"iwik?" ,"the old kiwi"]


class Mail(Cog):
    """
    Idiot!
    """

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def msgbox(self, ctx, *, the_text: str):
        open("assets/msg.txt", "a").write(f"{ctx.author.display_name} says: {the_text}\n")
        await ctx.message.reply("message stored!", mention_author=False)
    
    @commands.command()
    async def anonmail(self, ctx, *, the_text: str):
        """Sends mail to TBC's mailbox.

        This one is anonymous!

        - the_text
        The text to send to the mailbox"""
        channel = self.bot.get_channel(1281252582504923207)
        the_text = f"**FROM:" + random.choice(anon) + f"!**\n{the_text}"
        await channel.send(the_text)
        await ctx.message.reply("message sent!.", mention_author=False, delete_after=2,)
        await ctx.message.delete()
        
    # rip RBTXTE, where i learned how file edting worked
    @commands.command()
    async def msgbox(self, ctx, *, the_text: str):
        """This sends things to the messagebox.

        a time capsule that shall be opened on new years.
        
        - the_text
        The text to send to the messagebox"""
        open("assets/msg.txt", "a").write(f"{ctx.author.display_name} says: {the_text}\n")
        await ctx.message.reply("message stored!", mention_author=False)
        
        
    @commands.command()
    @commands.check(ismanager)
    async def newmsgbox(self, ctx, *, the_text: str):
        """This resets the messagebox.

        you get the first message too!
        
        -the_text
        First messagebox text."""
        open("assets/msg.txt", "w").write(f"{ctx.author.display_name} says: {the_text}\n")
        
    @commands.command()
    async def mail(self, ctx, *, the_text: str):
        """Sends mail to TBC's mailbox.

        This one uses your server nickname!

        - the_text
        The text to send to the mailbox"""
        channel = self.bot.get_channel(1281252582504923207)
        the_text = f"**FROM: {ctx.author.display_name}!**\n{the_text}"
        await channel.send(the_text)
        await ctx.message.reply("message sent!.", mention_author=False)

async def setup(bot):
    await bot.add_cog(Mail(bot))
