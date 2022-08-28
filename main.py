# Importing the discord package
import discord

# Declaring the intents
intents = discord.Intents.default()
intents.message_content = True

# Declaring the client
client = discord.Client(intents=intents)

# Declaring the 'on_ready' event
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Declaring the 'message' event
@client.event
async def on_message(message):

    if message.content.startswith('t!hello'):
        await message.channel.send('Hello!')

# Running the bot with the token
client.run('MTAwODM0MjQxNjE0MDU0NjA1OA.GMGk5V.t0FPjUIyHexxsuoWGWa-3t3ISywUnZCC7ALEEc')
