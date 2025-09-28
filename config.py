import os
from dotenv import load_dotenv
import discord

load_dotenv()


PREFIX = '!'
ROLE_NAME = 'Student'


TEST_GUILD_ID = 1415725752858574870
TEST_CHANNEL_ID = 1421452764868771890

intents = discord.Intents.default()

intents.members = True  # requires enabling the Privileged Intent in the Discord Developer Portal
intents.message_content = True  # safer default for slash‑only; set True if you still use prefix commands

# Token accessor
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')