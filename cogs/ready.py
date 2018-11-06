from discord.ext import commands


class Ready:

    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def on_ready():
        print("Ready!")

    @staticmethod
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return

        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send("This command can't be invoked in a DM channel!")

        elif isinstance(error, commands.MissingPermissions):
            print(error)
            await ctx.send("You haven't got the permission to execute this command!")
        else:
            print(error)
