import discord

client = discord.Client()


@client.event
async def on_message(message):
    # メッセージの送信者が、自分自身（BOT自身）であった場合
    if message.author == client.user:
        return  # 以降の部分を実行しない
    if message.content.startswith("こんにちは"):
        await message.channel.send("こんにちは！")

# トークンを入れてね
client.run("token")
