import discord, humanfriendly, datetime, yaml, termcolor
from time import mktime

def loadConfig():
    configFile = ""

    with open('config.yml', "r") as f:
            configFile = yaml.load(f, Loader=yaml.FullLoader)
    
    return configFile

config = loadConfig()

class Moderation(discord.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        termcolor.cprint(f"loaded moderation cog", "blue")
    
    @discord.slash_command(guild_ids=[config["guild_ID"]], description="Times out a member")
    @discord.default_permissions(manage_messages=True)
    @discord.option(
        "user",
        description="The user to timeout",
        required=True
    )
    @discord.option(
        "time",
        description="How long to timeout the user in the format 1h",
        required=True
    )
    @discord.option(
        "reason",
        description="Why the user has been timed out",
        required=False
    )
    async def timeout(self, ctx, user: discord.User, time: str, reason: str):
        timeSeconds = 0
        timeSeconds = humanfriendly.parse_timespan(time)
        
        timeoutTime=discord.utils.utcnow() + datetime.timedelta(seconds=timeSeconds)
        timeoutTimeUnix = timeoutTime.timestamp()

        await user.timeout(until=timeoutTime, reason=reason)
        userMessage = f"Timed out {user.mention} for {time}, expiring <t:{int(timeoutTimeUnix)}:R>"
        if reason == None:
            await ctx.respond(userMessage, ephemeral=True)
        else:
            await ctx.respond(f"{userMessage} with a reason of {reason}", ephemeral=True)

def setup(bot):
    bot.add_cog(Moderation(bot))