import os
import io
import discord
from discord.ext import commands

import re
import json

class kancolle:
    # def __init__(self, name, **kwargs):
    #     self.name = name
    #     for key, value in kwargs.items():
    #         setattr(self, key, value)
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_file(cls, filename):
        with open(f"data/kancolle/ship/{filename}", encoding="utf-8") as file:
            data = json.load(file)
            name = data.pop("name")
            return cls(name, **data)

    @classmethod
    def empty(cls, name):
        return cls(name, header=[], all_forms=[], quotes=[], character=None, notes=None, trivia=None, quests=None,
                   cg_art=[])

    def embed_form(self, cog):
        data_embed = discord.Embed(colour=discord.Colour.orange())
        data_embed.add_field(name=f" #{self.name}",
                             inline=False)
        check = len(self.header) + len(self.all_forms) + len(self.quotes) + len(self.cg_art)- 1
        for field in ("header", "all_forms", "quotes", "cg_art"):
            try:
                data = getattr(self, field)
                for stuff in data[:-1]:
                    data_embed.add_field(name=f"", value=stuff[1], inline=False)
                    check -= 1
                if check > 0:
                    data_embed.add_field(name=f"{data[-1][0]}",
                                         value=f"{data[-1][1]}\n----------------------------------------------------------------------------------",
                                         inline=False)
                else:
                    data_embed.add_field(name=f"", value=data[-1][1], inline=False)
                check -= 1
            except:
                pass
        pic_embed = discord.Embed(colour=discord.Colour.green())
        # pic_embed.set_image(url=self.true_url)
        return pic_embed, data_embed


class Kancolle:
    def __init__(self, bot):
        self.bot = bot
        self.kantai = {}
        for filename in os.listdir(f"data/kancolle/ship"):
            if filename.endswith('.json'):
                data = kancolle.from_file(filename)
                self.kantai[data.name] = data

    def _search(self, name, *, no_prompt=False):
        result = []
        try:
            d_id = str(name)
            if no_prompt:
                return self.kantai[d_id]
            else:
                return [self.kantai[d_id], ]
        except:
            pass
        regex = re.compile(".*?".join(name.split()), flags=re.I)
        for kantai in self.kantai.values():
            if regex.search(kantai.name):
                result.append(kantai)
            elif regex.search(kantai.alias):
                result.append(kantai)
        if no_prompt:
            for kantai in result:
                if name.lower() in (kantai.name.lower(), kantai.alias.lower()):
                    return kantai
            return result[0] if result else None
        else:
            return result

    async def filter(self, ctx, name, result, *, prompt_all=False):
        if not result:
            await ctx.send(f"Can't find {name} in database.")
            return None
        elif not prompt_all:
            if len(result) == 1:
                return result[0]
        await ctx.send("Do you mean:\n```\n{}\n<>: cancel\n```".format(
            '\n'.join([f"{index+1}: {d.name}" for index, d in enumerate(result)])))
        msg = await self.bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id)
        try:
            index = int(msg.content) - 1
        except:
            return None
        if index in range(len(result)):
            return result[index]
        else:
            return None

    @commands.command(aliases=["kancolle", ])
    async def kc(self, ctx, *, name: str):
        result = self._search(name)
        kancolle = await self.filter(ctx, name, result)
        if not kancolle:
            return
        pic_embed, data_embed = kancolle.embed_form(self)
        await ctx.send(embed=pic_embed)
        await ctx.send(embed=data_embed)
    # @commands.group()
    # async def kc(self, ctx):
    #     if ctx.invoked_subcommand is None:
    #         await ctx.send("`//kc s <Ship's name>, like: //kc s akebono kai ni`")


def setup(bot):
    bot.add_cog(Kancolle(bot))