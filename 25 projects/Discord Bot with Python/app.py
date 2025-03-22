import discord
import os
from discord.ext import commands

# Set up bot prefix
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm your Discord bot.")

@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

# Run bot with token from environment variable
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("Bot token not found. Set DISCORD_BOT_TOKEN as an environment variable.")
