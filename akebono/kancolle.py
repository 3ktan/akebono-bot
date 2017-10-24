import os
import io
import discord
from discord.ext import commands

import re
import json

class ship:
    def __init__(self, id, **kwargs):
        self.id = id
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def from_file(cls, filename):
        with open(f"data/test/{filename}", encoding="utf-8") as file:
            data = json.load(file)
            id = data.pop("id")
            return cls(id, **data)

    @classmethod
    def empty(cls, id):
        return cls(id, name=None, alias=None, pic_url=None, artwork_url=None, max_atk=0, max_hp=0, mlb_atk=None,
                   mlb_hp=None,
                   rarity=0, daemon_type=None, daemon_class=None, skill=[], ability=[], bond=[], additional_data={},
                   faction=None)

    def embed_form(self, cog):
        data_embed = discord.Embed(colour=discord.Colour.orange())
        data_embed.add_field(name=f"test",
                             value=f"\n----------------------------------------------------------------------------------",
                             inline=False)

        pic_embed = discord.Embed(colour=discord.Colour.orange())
        # pic_embed.set_image(url=self.true_url)
        return pic_embed, data_embed

class Kancolle:
    def __init__(self, bot):
        self.bot = bot

        self.daemons = {}
        for filename in os.listdir(f"data/test"):
            if filename.endswith('.json'):
                data = ship.from_file(filename)
                self.daemons[data.id] = data

        def _search(self, name, *, no_prompt=False):
            result = []
            try:
                d_id = int(name)
                if no_prompt:
                    return self.daemons[d_id]
                else:
                    return [self.daemons[d_id], ]
            except:
                pass
            regex = re.compile(".*?".join(name.split()), flags=re.I)
            for daemon in self.daemons.values():
                if regex.search(daemon.name):
                    result.append(daemon)
                elif regex.search(daemon.alias):
                    result.append(daemon)
            if no_prompt:
                for daemon in result:
                    if name.lower() in (daemon.name.lower(), daemon.alias.lower()):
                        return daemon
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


        @commands.command(aliases=["daemon", ])
        async def d(self, ctx, *, name: str):
            result = self._search(name)
            daemon = await self.filter(ctx, name, result)
            if not daemon:
                return
            pic_embed, data_embed = daemon.embed_form(self)
            # await ctx.send(embed=pic_embed)
            await ctx.send(embed=data_embed)




    # @commands.command(aliases=["kancolle", ])
    # async def kc(self, ctx, *, name: str):
    # # async def kc(self, ctx):
    #     with open("data/ship_list.txt", "r", encoding="utf-8") as ship:
    #         for line in ship:
    #             line = line.replace("\n","")
    #             with open("data/kancolle/ship/" + line + ".json", "r", encoding="utf-8") as data_file:
    #                 data = json.load(data_file)
    #                 name1 = data["all_forms"]["name"]
    #                 print(name1)
    #                 # if name is name1:
    #                 #     print(data["all_forms"]["id"])
    #                 #     break
    #                 # else:
    #                 #     continue
    #     # for name1 in name_list:
    #     #     if name is name1:
    #     #         print(data["all_forms"]["form"])
    #     print(data)

def setup(bot):
    bot.add_cog(Kancolle(bot))