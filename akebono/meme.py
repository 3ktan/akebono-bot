import discord
from discord.ext import commands
import random

class Meme:
    def __init__(self, bot):
        self.bot = bot
        self.links = {"bad": ("http://i.imgur.com/7Ny0ESJ.png",
                              "http://i.imgur.com/Z7dZfyl.jpg",
                              "http://i.imgur.com/NWbjLFL.gif",
                              "http://i.imgur.com/miuPFoR.jpg",
                              "http://i.imgur.com/z9V8maO.gif",
                              "http://i.imgur.com/2n8Ntpo.jpg",
                              "http://i.imgur.com/lL8PsVa.jpg",
                              "https://img4.hostingpics.net/pics/261404tumblrosktlcLFrl1qa94xto2500.gif",
                              "http://i.imgur.com/T8IAsHf.jpg",
                              ),

                      "fack": ( "http://i.imgur.com/0yNkFvN.jpg",
                                "http://i.imgur.com/yoE4tuK.jpg",
                                "http://i.imgur.com/v8pWOz4.jpg",
                                "http://i.imgur.com/rcG5dn3.jpg",
                                "http://i.imgur.com/L9XYqwr.jpg",
                                "http://i.imgur.com/I5l0ZuM.jpg",
                                ),
                      "haha": ("http://i.imgur.com/k7ebYah.jpg",
                               "http://i.imgur.com/YTuvyme.gif",
                               "http://i.imgur.com/fP3GWOF.png",
                               "http://i.imgur.com/3YhGzGH.gif",
                               "http://i.imgur.com/UBXGPX4.jpg",
                               "http://i.imgur.com/SWQcgX2.jpg",
                               "http://i.imgur.com/cp88PU3.gif",
                               "http://i.imgur.com/P7qfcqr.gif",
                           ),
                      "smug": ("http://i.imgur.com/OftBCI6.png",
                               "http://i.imgur.com/SYdxXzU.png",
                               "http://i.imgur.com/sGCgKiq.jpg",
                               "http://i.imgur.com/LUhs2gw.jpg",
                               "http://i.imgur.com/tbuSF7n.jpg",
                               "http://i.imgur.com/kyphT97.jpg",
                               "http://i.imgur.com/PPVZTXY.gif",
                               "http://i.imgur.com/o1JvcB9.jpg",
                               "http://i.imgur.com/LPJbWkH.jpg",
                               "http://i.imgur.com/7AlFiQx.jpg",
                               "http://i.imgur.com/7xPHpHj.jpg",
                               "https://cdn.discordapp.com/attachments/280534991685812235/332414832290562048/19399668_954326081373656_8260916710232556651_n.jpg",
                               "http://i.imgur.com/20FlrNU.jpg",
                               "http://i.imgur.com/yQBGvCJ.jpg",
                               "http://i.imgur.com/6SIiocG.jpg",
                               "http://i.imgur.com/SJFPRSX.jpg",
                               "http://i.imgur.com/9UxAzjQ.jpg",
                               "http://i.imgur.com/pjvmtQE.jpg",
                               "http://i.imgur.com/UU8ddwX.gif",
                               "http://i.imgur.com/ggg9W2c.png",

                           ),
                      "teehee": ("http://i.imgur.com/GOkAKvV.png",
                                 "http://i.imgur.com/ecWHIm0.png",
                                 "http://i.imgur.com/flC4HpD.png",
                                 "http://ddn.i.ntere.st/p/11192319/image",


                           ),
                      "waa": ("http://i.imgur.com/LgLzolV.gif",
                              "http://i.imgur.com/81r4YWU.jpg",
                              "http://i.imgur.com/ED5tyUZ.gif",
							  "https://media.giphy.com/media/2i0SGzoxG2WWs/giphy.gif",
							  "https://pbs.twimg.com/media/C3gPvdFUoAAi7rY.jpg",
							  "https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif",

                           ),
                      "wat": ("http://i.imgur.com/xBeUEmh.jpg",
                              "http://i.imgur.com/QEyMXCw.jpg",
                              "http://i.imgur.com/cbNegmA.jpg",
                              "http://i.imgur.com/5KeAhpE.jpg",
                              "http://i.imgur.com/AfzgsTO.jpg",
                              "http://i.imgur.com/Zkn67Wx.png",
                              "http://i.imgur.com/9V1ztaP.jpg",
                              "http://i.imgur.com/6HuNiHj.jpg",
                              "http://i.imgur.com/ARdiefz.png",
                              ),
                      "police": ("http://i.imgur.com/CYimeUd.jpg",
							"http://i.imgur.com/Jyzfm9o.jpg",
							"http://i.imgur.com/mU7O3uX.png",
							"http://i.imgur.com/9PPaV1i.jpg",
							"http://i.imgur.com/GcKhkyq.png",
							"http://i.imgur.com/g5EnTRo.jpg",
							"http://i.imgur.com/bX15Mvp.jpg",
							"http://i.imgur.com/RzBrjhc.gif",
							"http://i.imgur.com/MND5tpg.jpg",
							"http://i.imgur.com/A8Fmt4Z.png",
							"http://i.imgur.com/seUOidB.jpg",
							"http://i.imgur.com/bmjq17i.jpg",
                            "http://i.imgur.com/yNqtdVX.jpg",
                            ),
                      "salt": ("http://i.imgur.com/lzfdjBi.jpg",
                               "http://i.imgur.com/c0tnUoR.jpg",
                               "http://i.imgur.com/9FK4ETL.jpg",
                               "http://i.imgur.com/ZgxJgZ7.png",
                               "http://i.imgur.com/uUUY8tN.jpg",
                               "http://i.imgur.com/6iqquJw.gif",
                               "http://i.imgur.com/j0yJDwq.jpg",
                               "http://i.imgur.com/Zy4IQde.jpg",

                           ),
                      # "": ("",
                      #
                      #      ),
                      # "": ("",
                      #
                      #      ),
                      }
        for name, links in self.links.items():
            self.add_meme(name, links)

    def add_meme(self, name, links):
        setattr(self, "meme_" + name, [])
        for link in links:
            new_embed = discord.Embed()
            new_embed.set_image(url=link)
            getattr(self, "meme_" + name).append(new_embed)

    @commands.command()
    async def bad(self, ctx):
        await ctx.send(embed=random.choice(self.meme_bad))

    @commands.command()
    async def fack(self, ctx):
        await ctx.send(embed=random.choice(self.meme_fack))

    @commands.command()
    async def haha(self, ctx):
        await ctx.send(embed=random.choice(self.meme_haha))

    @commands.command()
    async def smug(self, ctx):
        await ctx.send(embed=random.choice(self.meme_smug))

    @commands.command()
    async def teehee(self, ctx):
        await ctx.send(embed=random.choice(self.meme_teehee))

    @commands.command()
    async def waa(self, ctx):
        await ctx.send(embed=random.choice(self.meme_waa))

    @commands.command()
    async def wat(self, ctx):
        await ctx.send(embed=random.choice(self.meme_wat))

    @commands.command()
    async def police(self, ctx):
        await ctx.send(embed=random.choice(self.meme_police))

    @commands.command()
    async def salt(self, ctx):
        await ctx.send(embed=random.choice(self.meme_salt))
def setup(bot):
    bot.add_cog(Meme(bot))
