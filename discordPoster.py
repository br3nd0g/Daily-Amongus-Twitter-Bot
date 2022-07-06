import os
import discord

disToken = os.environ['disBotKey']

client = discord.Client()


@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name="Daily Among Us"))
  print("Bot is ready!")


@client.event
async def on_message(message):
  if message.content.strip() == "|help":
    await message.channel.send("Hi! I am Daily Amongus. My prefix is | . The current available commands are\n|dailyAmongus")
  elif message.content.strip() == "|dailyAmongus":
    await message.channel.send(file=discord.File('currentAmong.png'))


async def runAmongBot():
  await client.run(disToken)
