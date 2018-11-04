import discord
import humanify


class Guild:

    @staticmethod
    def get(ctx):
        embed = discord.Embed(
            title=ctx.guild.name,
            description=f"👥Users: {len(ctx.guild.members)}\n"
                        f"🚩Roles: {len(ctx.guild.roles)}\n"
                        f"📰Channels: {len(ctx.guild.channels)}\n"
                        f"⏰Created-at: {humanify.datetime(ctx.guild.created_at)}",
            color=discord.Color.blue()
        )
        return embed


class Ping:

    @staticmethod
    def get(decode):
        embed = discord.Embed(
            description=f"Ping: **{decode}**",
            color=discord.Color.blue()
        )
        return embed


class Eval:

    @staticmethod
    def get(input, output):
        embed = discord.Embed(
            color=discord.Color.blue()
        )
        embed.add_field(
            name="__Input__",
            value=f"```py\n{input}```",
            inline=False
        )
        embed.add_field(
            name="__Output__",
            value=f"```py\n{output}```",
            inline=False
        )
        return embed
