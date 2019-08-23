import discord

client = discord.Client()

@client.event
async def on_message(message):
    # messageという変数の中に、メッセージに関するたくさんの情報が詰め込まれている。
    # 例):内容、送信者、チャンネル、送信時間・・・etc
    # どんな情報が含まれているかは、ここに載っている。
    # https://discordpy.readthedocs.io/ja/latest/api.html#message

    # メッセージの送信者が、自分自身（BOT自身）ではない場合に実行する
    # こうしないと、無限ループが発生してしまう。
    if message.author != client.user:
        # メッセージの内容を、メッセージの送られたチャンネルに送る。
        await message.channel.send(message.content)

# トークンを入れてね
client.run("token")