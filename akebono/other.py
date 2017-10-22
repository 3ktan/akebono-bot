import discord
from discord.ext import commands

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
        """Flip given text."""
        result = ""
        for char in msg:
            if char in self.text_flip:
                result += self.text_flip[char]
            else:
                result += char
        await ctx.send(content=result[::-1])

def setup(bot):
    bot.add_cog(Other(bot))