from discord.ext import commands
import discord
from discord import app_commands

class Command(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # A help command (slash)
    @app_commands.command(
        name="helpme",
        description="Pokazuje listę komend, lub wyjaśnia działanie funkcji podanej jako argument."
    )
    @app_commands.describe(komenda="Nazwa funkcji do wyjaśnienia (np. 'event', 'student', 'usun')")
    async def helpme(self, interaction: discord.Interaction, komenda: str | None = None):
        # Default general help
        embed = discord.Embed(
            title="ℹ️ Pomoc — Sensei SGGW v1.0.0",
            description="Lista komend:",
            color=discord.Color.green(),
        )
        embed.add_field(name="• /helpme", value="Zwraca listę komand z krótkimi opisami", inline=False)
        embed.add_field(name="• /helpme <nazwa funkcji>", value="Wyjaśnia działanie funkcji, wraz z przykładem", inline=False)
        embed.add_field(name="• /event", value="Tworzy wpis wydarzenia na kanał do wydarzeń", inline=False)
        embed.add_field(name="• /student", value="Nadaje rolę 'Student' użytkownikowi wywołującemu", inline=False)
        embed.add_field(name="• /usun", value="Usuwa rolę 'Student' użytkownikowi wywołującemu", inline=False)
        embed.set_footer(text="W przyszłości będzie więcej, chyba")

        # Context help based on argument
        if komenda:
            f = komenda.lower().strip()
            if f == "event":
                embed = discord.Embed(
                    title="📌 Pomoc: /event",
                    color=discord.Color.green(),
                )
                embed.description = (
                    "Składnia\n"
                    "```\n"
                    "!event <nazwa> <YYYY-MM-DD> [godzina] [miejsce]\n"
                    "```\n"
                    "• `<nazwa>` nazwa wydarzenia np: \"Chlanie\"\n"
                    "• `godzina` np. 14:00 (opcjonalne)\n"
                    "• `miejsce` miejsce wydarzenia (opcjonalne)\n"
                    "\n"
                    "🚨 Uwaga 🚨\n"
                    "Jeśli w polu `<nazwa>` chcemy podać tekst z odstępami\n"
                    "np: 'Chlanie z Dziekanem'\n"
                    "Koniecznie trzeba wpisać go w cudzysłowie:\n"
                    "```\n"
                    "!event \"Chlanie z Dziekanem\" [data] [czas] [miejsce]\n"
                    "```"
                )
            elif f == "student":
                embed = discord.Embed(
                    title="📌 Pomoc: /student",
                    description="Nadaje rolę 'Student' wywołującemu użytkownikowi.",
                    color=discord.Color.green(),
                )
            elif f == "usun":
                embed = discord.Embed(
                    title="📌 Pomoc: /usun",
                    description="Usuwa rolę 'Student' od wywołującego użytkownika.",
                    color=discord.Color.green(),
                )
            else:
                embed = discord.Embed(
                    title="❓ Nieznana funkcja",
                    description=f"Nie znam funkcji: `{komenda}`. Użyj `/helpme` bez argumentów, aby zobaczyć listę.",
                    color=discord.Color.orange(),
                )

        await interaction.response.send_message(embed=embed, ephemeral=False)


async def setup(bot: commands.Bot):
    await bot.add_cog(Command(bot))