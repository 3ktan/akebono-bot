import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import codecs
import json
import aiohttp
import lxml
import io

class test:
    '''
    Test something here before using
    '''

    def __init__(self, bot):
        self.bot = bot



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