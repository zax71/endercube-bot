"""
Endercube-bot by Zax71
Github: https://github.com/zax71/endercube-bot
"""
import discord, termcolor
from dotenv import load_dotenv

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Logged in as", bot.user)

bot.run()