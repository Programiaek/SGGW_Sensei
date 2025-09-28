import logging
import discord
from discord.ext import commands
from config import intents, PREFIX, DISCORD_TOKEN, TEST_GUILD_ID

# Makes discord.log file which helps with debugging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Create the bot (PREFIX is unused for slash‑only, but harmless)
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# A small helper to load all cogs
async def load_cogs():
    # Import here to avoid circular imports
    await bot.load_extension('cogs.events')
    await bot.load_extension('cogs.roles')
    await bot.load_extension('cogs.commands')

@bot.event
async def setup_hook():
    await load_cogs()
    try:
        guild = discord.Object(id=TEST_GUILD_ID)
        # Copy global commands into the guild view, then sync that guild
        bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)
        print(f"Slash commands synced to guild {TEST_GUILD_ID}")
    except Exception as e:
        print(f"Failed to sync app commands: {e}")

if __name__ == '__main__':
    if not DISCORD_TOKEN:
        raise RuntimeError('DISCORD_TOKEN is missing. Add it to your .env file.')
    bot.run(DISCORD_TOKEN, log_handler=handler, log_level=logging.DEBUG)