import discord


class Role:

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        await member.add_roles(member.guild.get_role(508651522683568130))
        await self.bot.get_channel(508654810606600195).send(embed=discord.Embed(title=f"HEY YOU {member.name}!", description="Welcome to Wambos Puff.\nEh yea, you got the Menschen Role and have fun here.", color=discord.Color.orange()))
