import discord

client = discord.Client()


@client.event
async def on_message(message):

    # メッセージの送信者が、自分自身（BOT自身）であった場合
    if message.author == client.user:
        return  # 以降の部分を実行しない

    # メッセージの内容が「こんにちは」で始まる場合
    if message.content.startswith("こんにちは"):
        # メッセージが送られたチャンネルに「こんにちは！(送信者の名前）さん！」と送信する
        await message.channel.send("こんにちは！{0.name}さん！".format(message.author))


# トークンを入れてね
client.run("token")
