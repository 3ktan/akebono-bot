from discord.ext import commands
from . import id
import random



def is_owner():
    async def check_func(ctx):
        if ctx.message.author.id == id.admin_id:
            return True
        else:
            x = random.choice(["Not Shitty Adminral, go away",
                               "...",
                               "Don't touch me!"
                               ])
            await ctx.send(x)
            return False
    return commands.check(check_func)


