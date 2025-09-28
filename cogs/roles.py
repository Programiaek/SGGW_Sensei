import discord
from discord.ext import commands
from discord import app_commands
from config import ROLE_NAME

class Roles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # /student — give the role to the invoking user
    @app_commands.command(name="student", description=f"Nadaje rolę '{ROLE_NAME}' użytkownikowi wywołującemu")
    async def student(self, interaction: discord.Interaction):
        if not interaction.guild:
            await interaction.response.send_message("Ta komenda działa tylko na serwerze.", ephemeral=True)
            return

        role = discord.utils.get(interaction.guild.roles, name=ROLE_NAME)
        if role:
            try:
                await interaction.user.add_roles(role, reason="/student command")
                await interaction.response.send_message(f"{interaction.user.mention} jest studentem, enjoy")
            except discord.Forbidden:
                await interaction.response.send_message("Nie mam uprawnień do nadawania ról.", ephemeral=True)
        else:
            await interaction.response.send_message("Nie mamy takiej roli xd", ephemeral=True)

    # /usun — remove the role from the invoking user
    @app_commands.command(name="usun", description=f"Usuwa rolę '{ROLE_NAME}' użytkownikowi wywołującemu")
    async def usun(self, interaction: discord.Interaction):
        if not interaction.guild:
            await interaction.response.send_message("Ta komenda działa tylko na serwerze.", ephemeral=True)
            return

        role = discord.utils.get(interaction.guild.roles, name=ROLE_NAME)
        if role:
            try:
                await interaction.user.remove_roles(role, reason="/usun command")
                await interaction.response.send_message(f"{interaction.user.mention} już nie jest studentem")
            except discord.Forbidden:
                await interaction.response.send_message("Nie mam uprawnień do usuwania ról.", ephemeral=True)
        else:
            await interaction.response.send_message("Nie mamy takiej roli xd", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Roles(bot))