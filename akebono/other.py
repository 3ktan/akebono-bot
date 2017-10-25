import discord
from discord.ext import commands
from akebono.utils import check
import random
from urllib.parse import quote_plus
import datetime
import aiohttp
import re


class Other:
    def __init__(self, bot):
        self.bot = bot
        self.youtube_regex = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')   #for seaching youtube, but maybe we do not need it

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
        x = random.choice([ "Why are you touching me? So annoying",
                           "What? What is it?",
                           "Why are you touching me? You don't stand a chance.",
                           "If you don't like me, why don't you remove me from the fleet (server)?",
                           "Really, being alone makes me feel relieved. I like being alone better... Yep.",
                           "Seriously, this is no joke.",
                           "If you don't like me, why don't you remove me from the fleet? ... It's not like it b-bothers me.",
                           "How many times, do I have to say before you understand!? What I hate the most is the shitty Admiral!! ...Why won't you believe what I said?",
                           "angry"])
        if (x =="angry"):
            embed = discord.Embed(title=":anger:", colour=discord.Colour.teal(), description=ctx.author.mention)
            embed.set_image(url="https://i.warosu.org/data/tg/img/0366/33/1418029945484.jpg")
            await ctx.send(embed=embed)
        else:
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

    @commands.command(pass_context=True, name='utb', no_pm=True)
    async def _youtube(self, ctx,*, context: str):
        try:
            url = 'https://www.youtube.com/results?'
            payload = {'search_query': ''.join(context)}
            headers = {'user-agent': 'Red-cog/1.0'}
            conn = aiohttp.TCPConnector()
            session = aiohttp.ClientSession(connector=conn)
            async with session.get(url, params=payload, headers=headers) as r:
                result = await r.text()
            session.close()
            yt_find = re.findall(r'href=\"\/watch\?v=(.{11})', result)
            url = 'https://www.youtube.com/watch?v={}'.format(yt_find[0])
            print(yt_find)
            embed = discord.Embed(
                title="Youtube",
                description="")
            embed.add_field(
                name="Other results for: " + context,
                value="https://www.youtube.com/watch?v=" + format(yt_find[1]) + ""
                    "\nhttps://www.youtube.com/watch?v=" + format(yt_find[2]) + ""
                    "\nhttps://www.youtube.com/watch?v=" + format(yt_find[3]) + ""
                    "\nhttps://www.youtube.com/watch?v=" + format(yt_find[4]) + ""
            )
            await ctx.send(url)
            await ctx.send(embed=embed)
        except Exception as e:
            message = "Something went terribly wrong! [{}]".format(e)
            await ctx.send(message)


def setup(bot):
    bot.add_cog(Other(bot))