"""
Endercube-bot by Zax71
Github: https://github.com/zax71/endercube-bot
"""
import discord, termcolor, yaml

def loadConfig():
    configFile = ""

    try:
        with open('config.yml', "r") as f:
            configFile = yaml.load(f, Loader=yaml.FullLoader)
    except:
        defaultConfig = open('defaultConfig.yml', "r")
        f = open('config.yml', 'w')
        f.write(defaultConfig.read())
    finally:
        with open('config.yml', "r") as f:
            configFile = yaml.load(f, Loader=yaml.FullLoader)
    
    return configFile


config = loadConfig()
bot = discord.Bot()

@bot.event
async def on_ready():
    print("Logged in as", bot.user)

bot.run(config["bot_token"])