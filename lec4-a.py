import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author != client.user:
        await message.channel.send(message.content)


client.run("token")