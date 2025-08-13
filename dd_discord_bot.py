from json import load as j_load
import discord
from discord.ext import commands
from lib_twitch_data_fetcher import get_dict_from_stream



##————————————————————————————————————————————————————————————————————————————##

bot = commands.Bot()



##————————————————————————————————————————————————————————————————————————————##

# From https://stackoverflow.com/questions/71165431/ , "pycord version" :
# Add the guild ids in which the slash command will appear.
# If it should be in all, remove the argument, but note that it will take some
# time (up to an hour) to register the command if it's for all guilds.

@bot.slash_command(
    name="first_slash",
    description="This is the first slash command.",
    guild_ids=[410481703958740992],
)

async def first_slash(ctx):
    await ctx.respond("You executed the slash command!")



@bot.slash_command(
    name="second_slash",
    description="This is the second slash command.",
    guild_ids=[410481703958740992],
)
async def second_slash(
        ctx, value: str = discord.Option(description="What I will echo")
    ):
    await ctx.respond(f"{value}")



@bot.slash_command(
    name="user_info",
    description="Get information about the user executing the command.",
    guild_ids=[410481703958740992],
)
async def user_info(ctx):
    user_id = ctx.author.id     # User ID
    username = ctx.author.name  # User name
    nickname = ctx.author.nick  # User nickname (None if not set)

    output = f"User ID: {user_id} \nUsername: {username} \n\
        Nickname: {nickname or 'No nickname set'}"

    await ctx.respond(output)



@bot.slash_command(
    name="stream_announcement",
    description="Annoncer un stream.",
    guild_ids=[410481703958740992],
)
async def second_slash(
        ctx,
        pseudo_twitch: str = discord.Option(description=
                                            "Le pseudonyme du compte Twitch."
                                            )
    ):
    await ctx.defer()

    config_file = "_config_twitch_api.json"

    user_nickname = ctx.author.nick

    info_dict = get_dict_from_stream(pseudo_twitch, config_file)
    title = info_dict["stream_title"]
    game = info_dict["game_name"]

    url = f"https://www.twitch.tv/{pseudo_twitch}"

    output = f"""
***EN LIVE***
**{user_nickname}** est en stream sur __{game}__ !
**{title}**
{url}
    """

    await ctx.respond(output)



##————————————————————————————————————————————————————————————————————————————##

if (__name__ == "__main__"):
    config_file = "_config_discord_api.json"

    with open(config_file) as file:
        credentials = j_load(file)

    discord_bot_token = credentials["discord_bot_token"]

    print("Running…")
    bot.run(discord_bot_token)


