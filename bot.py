import json
from discord.ext import commands
from utils import prefix
from cogs import ready, asign_role, basic_commands, prefix as pre

with open('secret.json', 'r') as fp:
    data = json.load(fp)


class Setup:
    def __init__(self):
        self.bot = commands.Bot(command_prefix=prefix.Prefix().set)
        self.bot.add_cog(ready.Ready(self.bot))
        self.bot.add_cog(asign_role.Role(self.bot))
        self.bot.add_cog(basic_commands.Basic(self.bot))
        self.bot.add_cog(pre.Prefix(self.bot))
        self.bot.run(data['token'])


Setup()
