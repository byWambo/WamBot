from discord.ext import commands
from utils import prefix


class Prefix:

    def __init__(self, bot):
        self.bot = bot
        self.forbidden = ["<@508652107172151306> ",
                          "<@!508652107172151306> "]

    @commands.group()
    async def prefix(self, ctx):
        """Custom Server Prefix System"""
        if ctx.invoked_subcommand is None:
            return

    @prefix.command(name='add')
    @commands.guild_only()
    @commands.has_permissions(manage_guild=True)
    async def _add(self, ctx, *args):
        """Adds a Prefix to the guild"""
        if not args:
            return await ctx.send("This command requires an argument.")

        if len(" ".join(args)) > 5:
            return await ctx.send("The prefix can't be longer, than 5 Chars.")

        return await prefix.Prefix.add_prefix(ctx, ctx.guild.id, args)

    @prefix.command(name='remove')
    @commands.guild_only()
    @commands.has_permissions(manage_guild=True)
    async def _remove(self, ctx, *args):
        """Removes a Prefix of the guild"""
        if args in self.forbidden:
            return await ctx.send("You can't remove this prefix!")

        return await prefix.Prefix.remove_prefix(ctx, ctx.guild.id, args)

    @prefix.command(name='list')
    @commands.guild_only()
    @commands.has_permissions(manage_guild=True)
    async def _list(self, ctx):
        """Shows all Prefixes of the guild"""
        return await ctx.send(f'These prefixes are on the Guild active: `' + " ".join(i for i in prefix.Prefix.get_prefix(ctx.guild.id, self.bot)) + "`")
