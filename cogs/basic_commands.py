import subprocess
import discord
from datetime import datetime
from discord.ext import commands
from utils import embeds


class Basic:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guild(self, ctx):
        """Sends information about this guild."""
        await ctx.send(embed=embeds.Guild.get(ctx))

    @commands.command()
    async def say(self, ctx, *text):
        """Says something."""
        if not text:
            return await ctx.send("This command requires arguments on what to say.")
        await ctx.send(embed=discord.Embed(description=" ".join(text), color=discord.Color.blue()))

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

    @commands.command(name="uptime")
    async def _uptime(self, ctx):
        """Tells you the uptime of the bot"""
        delta_uptime = datetime.utcnow() - self.bot.launch
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        return await ctx.send(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

