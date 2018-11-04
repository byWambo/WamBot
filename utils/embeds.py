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
