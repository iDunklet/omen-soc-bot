import discord
from discord.ext import commands
from discord import app_commands

from config import DISCORD_TOKEN, GUILD_ID

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    try:
        guild = discord.Object(id=GUILD_ID)
        synced = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)


@bot.tree.command(
    name="ping",
    description="Check bot status"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🏓 Pong!"
    )


bot.run(DISCORD_TOKEN)