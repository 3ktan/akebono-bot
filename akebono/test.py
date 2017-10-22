import discord
from discord.ext import commands
from bs4 import BeautifulSoup as BS
import urllib.request as rq
import codecs
import re
import json
import os
import asyncio

class test:
    def __init__(self, bot):
        self.bot = bot

    '''
    Test something here before using
    '''

    @commands.command()
    async def pm(self, user_id: str, *, content: str):
        user = await self.bot.get_user_info(user_id)

        fmt = content + '\n\n*This is a DM sent because you had previously requested feedback or I found a bug' \
                        ' in a command you used, I do not monitor this DM.*'

        try:
            await self.bot.send_message(user, fmt)
        except:
            await self.bot.say('Could not PM user by ID ' + user_id)
        else:
            await self.bot.say('PM successfully sent.')

    @commands.command()
    async def seach(self, ctx, *, name: str):
        data_embed =""
        try:
            with codecs.open("data/list_ship"+name+".json", encoding="utf-8") as file:
                jsonable = json.load(file)
                for key, value in jsonable.items():
                    data_embed = data_embed + str(key) + ": " + str(value) + "\n"

                embed = discord.Embed()
                embed.set_thumbnail(url="https://vignette2.wikia.nocookie.net/kancolle/images/e/ee/DD_Akebono_Kai_231_Card.jpg/revision/latest?cb=20161209135150")
                embed.add_field(
                    name="Here, it's the information analysis. ",
                    value=data_embed
                )
                embed.set_image(url="http://kancolle.wikia.com/wiki/Akebono?file=DD_Akebono_Kai_231_Card.jpg")
                await ctx.send(embed=embed)
        except:
            await ctx.send("No data.")

def setup(bot):
    bot.add_cog(test(bot))