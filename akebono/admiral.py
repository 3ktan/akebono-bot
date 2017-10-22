import discord
from discord.ext import commands
import random
from .utils import check

class admiral:
    def __init__(self,bot):
        self.bot = bot

########################## FUNCTIONS ##########################
    #reload one extension
    def reload_extension(self, extension):
        try:
            self.bot.unload_extension(extension)
            self.bot.load_extension(extension)
            print("Reloading " + extension + "...Done'")
        except Exception as e:
            print("Failed reloading {}: {}".format(extension, e))

    # reload all extension
    def reload_all_extensions(self):
        with open("extensions.txt") as file:
            extensions = [e for e in file.read().splitlines() if e]
        for extension in extensions:
            self.bot.unload_extension(extension)
        for extension in extensions:
            try:
                self.bot.load_extension(extension)
                print("Reloading " + extension + "...Done")
            except Exception as e:
                print("Failed reloading {}: {}".format(extension, e))

########################## ADMIN COMMANDS ##########################
    #reload extension(s)
    @commands.command()
    @check.is_owner()
    async def rl(self, ctx, extension: str = ""):
        print("Reloading module(s)...Please wait")
        if extension != "":
            await ctx.send("Reloading `"+ extension + "`...Please wait")
            extension = "akebono." + extension
            self.reload_extension(extension)
        else:
            await ctx.send("Reloading `all` extensions...Please wait")
            self.reload_all_extensions()
        print("All Done.")
        print("----------------------------")
        await ctx.send("Done")

    #change status
    @commands.command()
    @check.is_owner()
    async def status(self, ctx, *, stuff):
        await self.bot.change_presence(game=discord.Game(name=stuff))

    #logout! Bye bye
    @commands.command()
    @check.is_owner()
    async def logout(self, ctx):
        print("Thanks for the hard work!")
        await ctx.send("Thanks for the hard work!")
        await self.bot.logout()
######################### OTHER ############################3
    @commands.command()
    @check.is_owner()
    async def poke(self, ctx):
        x = random.choice(["Why are you touching me? So annoying",
                           "What? What is it?",
                           "Why are you touching me? You don't stand a chance.",
                           "If you don't like me, why don't you remove me from the fleet?",
                           "Really, being alone makes me feel relieved. I like being alone better... Yep.",
                           "Seriously, this is no joke.",
                           "If you don't like me, why don't you remove me from the fleet? ... It's not like it b-bothers me.",
                           "How many times, do I have to say before you understand!? What I hate the most is the shitty Admiral!! ...Why won't you believe what I said?",
                           ])
        await ctx.send(x)


def setup(bot):
    bot.add_cog(admiral(bot))