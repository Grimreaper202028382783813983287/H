import discord
from discord.ext import commands

client = commands.Bot(command_prefix="=", intents=discord.Intents.all())

@client.event 
async def on_ready():
    print("The bot is now ready for use!")
    print("-------------------------------")


@client.command()
async def ping(ctx):
    await ctx.send("Hello, I am the Grim Bot")

client.run('MTA5OTQ2ODIwNjU4Mzg0NDkwNQ.GkDjaU.uA9tIm84G0YnWzKNt3CEuMq_9QRM-yCEzXldvE')