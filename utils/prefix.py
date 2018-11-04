from discord.ext import commands
import json


class Prefix:

    def set(self, bot, message):
        prefixes = ['sudo ']
        prefixes.extend(self.get_prefix(message.guild.id, bot))
        return commands.when_mentioned_or(*prefixes)(bot, message)

    @staticmethod
    def get_prefix(guild_id, bot):
        with open("utils/prefix.json", "r") as fp:
            data = json.load(fp)
        try:
            return data[str(guild_id)]
        except KeyError:
            with open('utils/prefix.json', 'w') as fp:
                data[str(guild_id)] = [f'<@{bot.user.id}> ', f'<@!{bot.user.id}> ']
                json.dump(data, fp, sort_keys=True, indent=2)
            return data[str(guild_id)]
