import random
from urllib.parse import quote
from discord.ext import commands


class Retard:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="retard")
    async def _retard(self, ctx, *, text: str):
        """Translates some normal text to retard language."""

        await ctx.send("".join([random.choice([char.upper(), char.lower()]) for char in text]))

    @commands.command(name="retardish")
    async def _retardish(self, ctx, *text: str):
        """Lets retardish the text"""
        if not text:
            return await ctx.send("How about a text, to make it retardish?")
        words = list(text)
        random.shuffle(words)

        await ctx.send(" ".join(words))

    @commands.command(name="lmgtfy", aliases=["google", "search"])
    async def _lmgtfy(self, ctx, *args):
        """Shows how to google."""
        if not args:
            return await ctx.send("This command requires arguments.")
        query = quote(" ".join(args))
        await ctx.send(f"huh? Let me show you how to type this `{' '.join(args)}` in google.\n"
                       f"<http://lmgtfy.com/?q={query}>")

    @commands.command(name="yt")
    async def yt(self, ctx, *text):
        """Searches something on YouTube"""
        if not text:
            return await ctx.send("This command requires arguments.")
        query = quote(" ".join(text))
        await ctx.send(f"Here the query. https://www.youtube.com/results?search_query={query}")
