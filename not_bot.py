import discord
from discord.ext import commands

def _callable_prefix(bot, message):  # Die Parameter übergibt die Commands-Extension
    prefixes = ['sudo ']
    prefixes.extend(get_prefix(message.guild.id))
    return commands.when_mentioned_or(*prefixes)(bot, message)


def get_prefix(guildid):
    if guildid == 444144150443458571:
        return "!"
    else:
        return "?"


bot = commands.Bot(command_prefix=_callable_prefix)


async def on_message(message):
    await bot.process_commands(message)


class Meh:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Hi")
    async def hi(self, ctx):
        await ctx.send("Hi")


bot.add_cog(Meh(bot))
bot.run("NDU0MjU1MDI2MjM2MjkzMTIw.Dr3-7Q.6TNIcCxSoIBgmM2fs04XFqVMJGU")
