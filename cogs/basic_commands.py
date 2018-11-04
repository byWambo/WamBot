import subprocess
import asyncio
from discord.ext import commands
from utils import embeds


class Basic:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guild(self, ctx):
        await ctx.send(embed=embeds.Guild.get(ctx))

    @commands.command()
    async def say(self, ctx, *text):
        if not text:
            return await ctx.send("This command requires arguments on what to say.")
        await ctx.send(" ".join(text))

    @commands.command(name="ping")
    async def _ping(self, ctx):
        """Shows an actual, real ping to discordapp.com"""

        cmd = "ping discordapp.com"
        await ctx.trigger_typing()
        try:
            exc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            result = str(exc.communicate()[0].splitlines()[2])
            begin = result.find('t=')
            end = result.find('TTL')
            await ctx.send(embed=embeds.Ping.get(result[begin + 2:end]))
        except IndexError:
            await ctx.send(embed=embeds.Ping.get('Host down!'))
