from datetime import datetime
from time import sleep
from mcstatus import JavaServer
import discord
from discord.ext import commands

#Minecraft
server = JavaServer("193.135.10.132", 15550)
status = server.status()

#Discord
TOKEN = ''
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

async def editembed():
    status = server.status()
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    new_embed = discord.Embed(
        title = 'Niklas Minecraft Server Status',
        description = 'zwerg lol',
        colour = discord.Colour.blurple()
    )

    new_embed.set_footer(text=f"Last update: {time}")
    new_embed.set_image(url='https://cdn.discordapp.com/attachments/871187487815503902/987455284375060551/WhatsApp_Image_2022-06-11_at_12.10.17.jpeg')
    new_embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/871187487815503902/984999860585521162/pack__1_.jpg')
    new_embed.set_author(name=f"{client.user.name} Minecraft Server Watcher", icon_url=client.user.avatar_url)
    new_embed.add_field(name='Version', value=status.version.name, inline=False)
    new_embed.add_field(name='Latency:', value=f"{int(status.latency)} ms", inline=False)
    new_embed.add_field(name='Players online:', value=f"{status.players.online}/{status.players.max}", inline=False)
    
    return new_embed

@client.command()
async def displayembed(ctx):
    status = server.status()
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    embed = discord.Embed(
        title = 'Niklas Minecraft Server Status',
        description = 'zwerg lol',
        colour = discord.Colour.blurple()
    )

    embed.set_footer(text=f"Last update: {time}")
    embed.set_image(url='https://cdn.discordapp.com/attachments/871187487815503902/987455284375060551/WhatsApp_Image_2022-06-11_at_12.10.17.jpeg')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/871187487815503902/984999860585521162/pack__1_.jpg')
    embed.set_author(name=f"{client.user.name} Minecraft Server Watcher", icon_url=client.user.avatar_url)
    embed.add_field(name='Version', value=status.version.name, inline=False)
    embed.add_field(name='Latency:', value=f"{int(status.latency)} ms", inline=False)
    embed.add_field(name='Players online:', value=f"{status.players.online}/{status.players.max}", inline=False)
    
    

    msg = await ctx.send(embed=embed)
    print(f"Created initial message embed on {time}")

    while True:
        updated_msg = await editembed()
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        await msg.edit(embed = updated_msg)
        print(f"Edited message embed on {time}")
        sleep(60)

client.run(TOKEN)