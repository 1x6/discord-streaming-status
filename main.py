import discord

from discord.ext import tasks, commands

client = commands.Bot(
    command_prefix=':',
    self_bot=True
)


@client.event
async def on_connect() :
    await client.change_presence(activity=discord.Streaming(name="yes", url="https://www.twitch.tv/yougotsyskeyed"))


client.run('account token', bot=False)
