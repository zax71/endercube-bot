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
        termcolor.cprint("Loaded moderation cog", "blue")
    
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

    @discord.slash_command(guild_ids=[config["guild_ID"]], description="Bans a member")
    @discord.default_permissions(manage_messages=True)
    @discord.option(
        "user",
        description="The user to ban",
        required=True
    )
    @discord.option(
        "reason",
        description="Why the user has been banned",
        required=False
    )
    @discord.option(
        "delete_messages",
        description="How far back should we delete the users messages? Max 7 days",
        required=False,
        input_type=int,
        default=0,
        min_value=0,
        max_value=7
    )
    async def ban(self, ctx, user: discord.Member, reason: str, delete_messages: int):

        await ctx.guild.ban(user, reason=reason, delete_message_days=delete_messages)
        userMessage = f"Banned {user.mention} and deleted messages for {delete_messages} days"
        if reason == None:
            await ctx.respond(userMessage, ephemeral=True)
        else:
            await ctx.respond(f"{userMessage} with a reason of {reason}", ephemeral=True)
    
    @discord.slash_command(guild_ids=[config["guild_ID"]], description="Kicks a member")
    @discord.default_permissions(manage_messages=True)
    @discord.option(
        "user",
        description="The user to kick",
        required=True
    )
    @discord.option(
        "reason",
        description="Why the user has been kicked",
        required=False
    )
    async def kick(self, ctx, user: discord.User, reason: str):
        await user.kick(reason=reason)
        userMessage = f"Kicked {user.mention}"
        
        if reason == None:
            await ctx.respond(userMessage, ephemeral=True)
        else:
            await ctx.respond(f"{userMessage} with a reason of {reason}", ephemeral=True)

def setup(bot):
    bot.add_cog(Moderation(bot))