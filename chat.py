import discord
import random
import time
import asyncio
from discord.ext import commands
import discordSuperUtils

bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())
ReactionManager = discordSuperUtils.ReactionManager(bot)

TOKEN="OTQ2NDAxNDg0OTIzMzY3NDM1.YheLEQ.vEBYzoaPIDN36y3T-v9TozWQ2zo"

client= discord.Client()
abuses= ("fuck","dumbass", "motherfucker")
greetings = ("Hi","hi","wasup","hey","greetings")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(greetings):
       await message.channel.send("Hi welcome to our community where we raise and grow talents THE TECH TYCOON")

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_ready():
    print("running")


@ReactionManager.event()
async def on_reaction_event(guild, channel, message, member, emoji):
    """This event will be run if there isn't a role to add to the member."""

    if ...:
        print("Created ticket.")


@bot.event
async def on_ready():
    database = discordSuperUtils.DatabaseManager.connect(...)
    await ReactionManager.connect_to_database(database, ["reaction_roles"])

    print("Reaction manager is ready.", bot.user)


@bot.command()
async def reaction(
    ctx, message, emoji: str, remove_on_reaction, role: discord.Role = None
):
    message = await ctx.channel.fetch_message(message)

    await ReactionManager.create_reaction(
        ctx.guild, message, role, emoji, remove_on_reaction
    )

client.run(TOKEN)
print(client.user.name)
