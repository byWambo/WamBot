from discord.ext import commands
import json


class Prefix:

    def set(self, bot, message):
        try:
            prefixes = []
            prefixes.extend(self.get_prefix(message.guild.id, bot))
            return commands.when_mentioned_or(*prefixes)(bot, message)
        except AttributeError:
            return commands.when_mentioned_or('sudo')(bot, message)

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

    @staticmethod
    async def add_prefix(ctx, guild_id, prefix):
        with open('utils/prefix.json', 'r') as fp:
            data = json.load(fp)
        if len(data[str(guild_id)]) == 5:
            return await ctx.send("You already got 5 Prefixes!")
        _list = data[str(guild_id)]
        new = _list.insert(0, " ".join(prefix))
        print(new)
        _list = new
        with open('utils/prefix.json', 'w') as fp:
            json.dump(data, fp, indent=2, sort_keys=True)
        return await ctx.send('Successfully added this prefix!')

    @staticmethod
    async def remove_prefix(ctx, guild_id, prefix):
        with open('utils/prefix.json', 'r') as fp:
            data = json.load(fp)
        _list = data[str(guild_id)]
        if not "".join(prefix) in _list:
            return await ctx.send("You haven't got this prefix!")
        new = _list.remove(" ".join(prefix))
        _list = new
        with open('utils/prefix.json', 'w') as fp:
            json.dump(data, fp, indent=2, sort_keys=True)
        return await ctx.send('Successfully deleted this prefix!')
