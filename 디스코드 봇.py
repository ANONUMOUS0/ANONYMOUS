import discord
import os

client = discord.Client()



@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("구매문의 익명#4735")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("반가워")
    if message.content.startswith("뭐해"):
        await message.channel.send("익명샵에서 핵사는중")
    if message.content.startswith("놀자"):
        await message.channel.send("구매하면 놀아줄게")

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))




access_token = os.environ["BOT_TOKEN"]
client.run("NTg1ODE1Njg2MzE2NTU2MzE4.XPe9vQ.rSfRk1vU6nAaFA-ORpOQSgs2IaU")

