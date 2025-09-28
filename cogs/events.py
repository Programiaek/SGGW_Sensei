from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Message to the terminal when the bot is ready
    @commands.Cog.listener()
    async def on_ready(self):
        # Using self.bot for consistency
        print(f'{self.bot.user.name} has connected to Discord!')

    # Message to the new members
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(f"Witaj na serwerze informatyku, masz ze sobą piwo {member.mention}?")

async def setup(bot: commands.Bot):
    await bot.add_cog(Events(bot))