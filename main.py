import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    await bot.load_extension("anonymous")
    await bot.tree.sync()
    print(f"✅ البوت شغالة: {bot.user}")

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
