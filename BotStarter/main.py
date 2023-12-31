import discord
from discord.ext import commands
from info.config import TOKEN
import os
import asyncio

bot = commands.Bot(command_prefix="*", help_command=None, intents=discord.Intents.all())

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())