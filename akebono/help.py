import discord
from discord.ext import commands


class Help_module:
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")

    @commands.group()
    async def help(self, ctx ):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                title=self.bot.user.name,
                colour=discord.Colour.teal(),
                description="Description: Phantasy Star Online 2 & Kantai Collection (kancolle)")
            embed.add_field(
                name="Standard Commands List ",
                value="`//inv`: Invite bot to your server"
                      "`//about:` description about Bot & Athor\n"
                      "`//help user:` Get information about a user \n"
                      "`//help meme`: List meme\n"
                      "`//help pso2`: Phantasy Star Online 2")
            await ctx.send(embed=embed)


    @commands.command()
    async def inv(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.teal(),
            )
        embed.add_field(
            name="Invite Link:",
            value="https://goo.gl/mnZcsw"
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(
            title=self.bot.user.name,
            colour=discord.Colour.teal(),
            description="Description: Phantasy Star Online 2 & Kantai Collection (kancolle)\n"
                        "Support: https://discord.gg/86SXwYJ \n"
                        "Invite bot to your server: https://goo.gl/mnZcsw"
        )
        embed.add_field(
            name="Athor: 3ktan",
            value="Facebook: https://www.facebook.com/3ktan/\n"
                  "Wordpress: http://3ktan.wordpress.com/\n"
                  "Twitter: https://twitter.com/3ktan/",
            inline=True
        )
        embed.set_thumbnail(
            url="http://i.imgur.com/Qvqj5n9.jpg"
        )
        await ctx.send(embed=embed)

    @help.command()
    async def user(self, ctx):
        embed = discord.Embed(
            title="//user",
            colour=discord.Colour.teal(),
            description="Infomations about user in the server")
        embed.add_field(
            name="Standard Commands List ",
            value= "`//user, `//info, `//userinfo` : Infomations about user: id, status, roles,...\n"
                   "`//avatar`: Fetch and display the requested users avatar.\n"
                   "etc: `//user` or `//user @Akebono#2673`"
                    )
        await ctx.send(embed=embed)

    @help.command()
    async def pso2(self, ctx):
        embed = discord.Embed(
            title="//pso2",
            colour=discord.Colour.teal(),
            description="Phantasy Star Online 2 ")
        embed.set_thumbnail(url="http://ww3.sinaimg.cn/crop.0.0.600.337.1000.562/4e4baa2egw1f6i46t0n7oj20go0a940q.jpg")
        embed.add_field(
            name="Standard Commands List ",
            value= "`//pso2`: Link Related to PSO: bumped, swiki,..\n"
                   )
        await ctx.send(embed=embed)

    @help.command()
    async def meme(self, ctx):
        embed = discord.Embed(
            title="//meme",
            colour=discord.Colour.teal(),
            description="")
        embed.add_field(
            name="Meme list",
            value="`//bad`: \n"
                  "`//fack`: \n"
                  "`//haha`: \n"
                  "`//smug`: \n"
                  "`//teehee`: \n"
                  "`//waa`: \n"
                  "`//wat` \n"
                  "`//police`: Hello onni-chan. \n"
                  "`//salt`: want some salt\n"
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help_module(bot))