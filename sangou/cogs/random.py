import discord
import os
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import Cog
import html
import json
import requests


class Random(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def peppino(self, ctx):
        """Posts a random Peppino.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/peppino"

        lines = [
            "What do you know about this tower? Who are you? I don't know anything!",
            "Did you know you could do a flying uppercut by pressing [up] then [grab]? This can work as a pseudo double jump and can also dispatch enemies in the air!",
            "After dispatching a few enemies, you might have noticed the electricity effect around you. While the effect is active, press [up] then [taunt] to dispatch every enemy on the screen!",
            "Did you know that your full name is Peppino Spaghetti? That's unfortunate.",
            "If you hurt Peppino too much, you can go to hell!",
            "Did you know that you can block and parry any projectile or damage by pressing [taunt] before getting hurt?",
            "I'm going to go ahead and talk about something that I've been telling others who know about this place of worship that you did this. Well, we're down from your pizzeria, and we're down from this tower. There are customers, and they want to see one of these things. So I got a friend, he went down one of the floors and this guy came up next to me, and the idea was, why is it that when you're in the upper part of the tower there is this Pizzaface character, then there's a man from your previous life leading the way? There's a pizza in your tower with all this information.",
            "I wouldn't trust this Gustavo guy... He seems a bit too friendly...",
            "Once you have beaten a level, you can revisit it to find a Lap 2 portal near the entrance. These will give you a point bonus, but also force you to loop around the escape portion one more time...",
            "I've lost my medication again. This day is going to suck!",
            "Pizza Tower Instant Pizza Gaming Promotion! Type pizza to order a free pizza courtesy of Peppino's Pizza!",
            "Did you know that you can do a piledriver by holding an enemy and pressing [down] while in the air? You can also perform a piledriver that will boost you upward if you hold [up] before grabbing an enemy.",
            "Remember to not take too many breaks, keep playing! Your time here is limited!",
            "An obscure technique: While doing a dive in the air and pressing [jump], you will directly go downward with a body slam. Only useful if you want to save time!",
            "Do you seriously think that I'm going to give you more advice after that blunder you just did?",
            "Did you know that you can make enemies react to you faster by pressing [taunt] near them?",
            "I don't think you need any hints today.",
            "Does your fridge smell weird? Have you checked the expiration date?",
            "The elusive P rank... You can get it by doing everything there is to do in a level. The problem is that you need to keep a combo for the entirety of the level! It's a tough challenge, so don't feel bad if you don't want to do it!",
            "You know, you really could lose some weight.",
            "Are you going to play or just stand there stupidly?",
            "Kiss my ass!",
        ]

        await ctx.reply(
            content=random.choice(lines),
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def cat(self,ctx):
        """gives you a cat

        meow :3
        not beating the furry allegations...

        No arguments."""
        catr = requests.get("https://api.thecatapi.com/v1/images/search?size=small")
        if catr.status_code == 200:
            imgurc = catr.json()[0]['url']
            await ctx.reply(imgurc, mention_author=False)
        else:
            await ctx.reply("cats are too angry to send right now...", mention_author=False)
            
            
    @commands.command()
    async def dog(self,ctx):
        """gives you a dog

        they will eat all your plastic

        No arguments."""
        dogr = requests.get("https://api.thedogapi.com/v1/images/search?size=small")
        if dogr.status_code == 200:
            imgurd = dogr.json()[0]['url']
            await ctx.reply(imgurd, mention_author=False)
        else:
            await ctx.reply("dogs are being too much trouble to send right now...", mention_autor=False)
            
    @commands.command()
    async def fox(self,ctx):
        """gives you a fox

        they are quite silly

        No arguments."""
        foxr = requests.get("https://randomfox.ca/floof/")
        if foxr.status_code == 200:
            imgurf = foxr.json()['image']
            await ctx.reply(imgurf, mention_author=False)
        else:
            await ctx.reply("foxes got rabies and cant be sent right now...", mention_autor=False)
            
    @commands.command()
    async def duck(self,ctx):
        """gives you a duck

        The season finale of duck-tective!

        No arguments."""
        ducker = requests.get("https://random-d.uk/api/v2/random")
        if ducker.status_code == 200:
            imgurdu = ducker.json()['url']
            await ctx.reply(imgurdu, mention_author=False)
        else:
            await ctx.reply("duck-tective was killed by his evil twin brother, and cant be sent right now...", mention_autor=False)
    
    
    @commands.command()
    async def noise(self, ctx):
        """Posts a random Noise.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/noise"

        lines = [
            "Instead of running up walls, Noise will bounce off them with his skateboard. While doing a wall bounce, press [grab] to launch yourself in the direction of a wall in order to bounce again.",
            "Noise can do a drill move if [down] is held while he is in the air and his skateboard is out. While doing the drill move, you can move left and right freely. You will also go through small gaps automatically.",
            "Noise's Super Jump works the same, but he has the ability to do it at any moment by pressing [left] and [right] while on the ground.",
            "When doing a wall bounce, keep [dash] held while reaching the ground to boost forward!",
            "Did you know that your full name is Theodore Noise? That's unfortunate.",
            "I wouldn't trust this Noisette gal... Wait, she's your girlfriend?",
            "If you hurt The Noise too much, nothing happens!",
            "Pizza Tower Instant Pizza Gaming Promotion! Type pizza to order a free pizza courtesy of Noise's Pizza!",
            "Remember that you can do your Super Jump at any time! This should give you an advantage over some other italian dude...",
            "Weren't you supposed to bring your rat friend? No matter, you can still do [U][J] in the air to do the crusher jump. It should get you through these upcoming sections!",
        ]
        await ctx.reply(
            content=random.choice(lines),
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def rat(self, ctx):
        """Posts a random Rat.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/rat"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def gustavo(self, ctx):
        """Posts a random Gustavo.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/gustavo"

        lines = [
            "Hold [dash] to move faster and destroy metal blocks!",
            "Press [up][grab] to kick the rat!",
            "Press [jump] in the air to do a double jump! You can cancel out of it with another move too!",
            "Press [down] middair to quickly go down!",
            "The double jump can also destroy metal blocks underneath!",
            "While doing the double jump, hold [jump] while holding in the direction of a wall to climb it!",
        ]

        await ctx.reply(
            content=random.choice(lines),
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def bench(self, ctx):
        """Posts a random Bench.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/bench"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )


async def setup(bot):
    await bot.add_cog(Random(bot))
