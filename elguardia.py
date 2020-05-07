# -*- coding: utf8 -*-

import discord
from discord.ext import commands, tasks
import datetime
import requests
import random
# import PyNaCL

canales = {'pastos':705421710819721326, 'sala': 702167241634087094, 'lol': 702168817400545291,'magic': 707410238814552137, 'minecraft': 702184813377093684, 'smite': 707766639558525018, 'afk': 702186742324658177, 'test':707719786741628963}
currentChanell = None
bot = commands.Bot(command_prefix='-')

paqueosPool = [
    'a ver muestrenme sus credenciales',
    '\*foto a la credencial\* esto le va a llegar a su jefe de carrera',
    'ya chicos retirense',
    '\*Por la radio\* atención, hay un grupo sospechoso en los pastos',
    'Creen que soy wn, que no me doy cuenta lo que hacen'  ,
    'tenemos un 3312',
    'Ya chicos, se puede estar dentro de la universidad solo hasta las 9 vayan saliendo'
]

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def paquear(ctx, *args):
    if (len(args) > 0):
        await connectToVoiceChannel(args[0])
        return
    paqueo = random.choice(paqueosPool)
    await ctx.send(paqueo)

@bot.command()
async def guardia(ctx, *arg):
    print('guardia')
    paqueo = random.choice(paqueosPool)
    await ctx.send(paqueo)

@tasks.loop(seconds=60)
async def irAPaquear():
    randomKey = random.choice(list(canales.keys()))
    print('move to:', randomKey)
    await connectToVoiceChannel()


async def connectToVoiceChannel(key):
    if key in canales:
        if len(bot.voice_clients) > 0:
            await bot.voice_clients[0].disconnect()
        channelId = canales[key]
        print(type(channelId), channelId)
        channel = bot.get_channel(channelId)
        await channel.connect()

irAPaquear.before_loop(bot.wait_until_ready)    
irAPaquear.start()
bot.run('NzA3NzE3OTcxNzk0OTg0OTYw.XrM9Ew.2dFPeTnnTMOyvT7pbWzLFlwxrzQ')