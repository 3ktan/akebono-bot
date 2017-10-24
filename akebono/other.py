import discord
from discord.ext import commands
from akebono.utils import check
import random
from urllib.parse import quote_plus
import aiohttp




class Other:
    def __init__(self, bot):
        self.bot = bot

    #flip text
    text_flip = {}
    char_list = "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}"
    alt_char_list = "{|}zʎxʍʌnʇsɹbdouɯlʞɾᴉɥƃɟǝpɔqɐ,‾^[\]Z⅄XMΛ∩┴SɹQԀONW˥ʞſIHפℲƎpƆq∀@¿<=>;:68ㄥ9ϛㄣƐᄅƖ0/˙-'+*(),⅋%$#¡"[::-1]
    for idx, char in enumerate(char_list):
        text_flip[char] = alt_char_list[idx]
        text_flip[alt_char_list[idx]] = char
    @commands.command(pass_context=True)
    async def textflip(self, ctx, *, msg):
        result = ""
        for char in msg:
            if char in self.text_flip:
                result += self.text_flip[char]
            else:
                result += char
        await ctx.send(content=result[::-1])

    #poke bot _(:3
    @commands.command()
    async def poke(self, ctx):
        x = random.choice(["Why are you touching me? So annoying",
                           "What? What is it?",
                           "Why are you touching me? You don't stand a chance.",
                           "If you don't like me, why don't you remove me from the fleet (server)?",
                           "Really, being alone makes me feel relieved. I like being alone better... Yep.",
                           "Seriously, this is no joke.",
                           "If you don't like me, why don't you remove me from the fleet? ... It's not like it b-bothers me.",
                           "How many times, do I have to say before you understand!? What I hate the most is the shitty Admiral!! ...Why won't you believe what I said?",
                           ])
        await ctx.send(x)

    #ping
    #i have no idea why i code this
    @commands.command(hidden=True)
    async def ping(self, ctx):
        await ctx.send("Pong")

    # countdown
    @commands.command(name='countdown', hidden=True)
    async def countdown(self, ctx, seconds: int):
        from asyncio import sleep
        if seconds > 3600:
            await ctx.send(
                "{}, I cannot count down for anytime longer than 3600 seconds".format(ctx.author.mention))
            return
        else:
            em = discord.Embed(title="countdown", description=str(seconds))
            count = await ctx.send(embed=em)
            sleep(1)
            for i in list(range(seconds))[::-1]:
                em = discord.Embed(title="countdown", description=i)
                await count.edit(embed=em)
                await sleep(1)
            await count.delete()
            await ctx.send(format(ctx.author.mention) + ", countdown from `" + str( seconds) + "`: Done")



def setup(bot):
    bot.add_cog(Other(bot))