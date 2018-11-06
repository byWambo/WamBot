import json
from datetime import datetime
from discord.ext import commands
from utils import prefix
from cogs import ready, asign_role, basic_commands, prefix as pre

with open('secret.json', 'r') as fp:
    data = json.load(fp)

cogs = [
    ''
]


class WamBot(commands.AutoShardedBot):
    """This is a subclass, for more things."""
    def __init__(self):
        super().__init__(
            command_prefix=prefix.Prefix().set,
            description='A hopefully nice Discord bot',
            owner_id=273850063153790977,
            fetch_offline_members=False
        )

        self.launch = datetime.utcnow()
        self.version = '0.0.1a'


class Setup:
    def __init__(self):
        self.bot = WamBot()
        self.bot.add_cog(ready.Ready(self.bot))
        self.bot.add_cog(asign_role.Role(self.bot))
        self.bot.add_cog(basic_commands.Basic(self.bot))
        self.bot.add_cog(pre.Prefix(self.bot))
        self.bot.run(data['token'])


Setup()
