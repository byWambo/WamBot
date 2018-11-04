from discord.ext import commands
from utils import embeds


class Basic:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guild(self, ctx):
        await ctx.send(embed=embeds.Guild.get(ctx))
