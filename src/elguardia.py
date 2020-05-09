# -*- coding: utf8 -*-

import discord
from discord.ext import commands, tasks
import datetime
import requests
import random
import os
import asyncio
# import PyNaCL

canales = {'pastos':705421710819721326, 'salita uwu': 702167241634087094, 'lol': 702168817400545291,'magic': 707410238814552137, 'minecraft': 702184813377093684, 'smite': 707766639558525018, 'afk': 702186742324658177, 'test':707719786741628963, 'valorant': 707766639558525018}
currentChanell = None
bot = commands.Bot(command_prefix='-')

token=os.environ.get('elGuardiaToken',"")

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
    bot.loop.create_task(irAPaquear())

@bot.command()
async def paquear(ctx, *args):
    if (len(args) > 0):
        if (args[0].lower() == 'guetti'):
            await ctx.send('Guetti deja el lol')
            return
        if (args[0].lower() == 'lixo'):
            await ctx.send('Cortese el pelo jipy')
            return
        if (args[0].lower == 'joelo'):
            await ctx.send('ya, pa que tan sangron')
            return
        await connectToVoiceChannel(args[0])
        return
    paqueo = random.choice(paqueosPool)
    await ctx.send(paqueo)

@bot.command()
async def guardia(ctx, *args):
    print('guardia')
    if (args[0] == 'dar' and args[1] == 'comida' and len(args) > 2):
        r1 = '\*Se como el {}\* Gracias estaba muy bueno'.format(args[2])
        r2 = 'No gracias, no como en el trabajo'
        await ctx.send(r1 if random.random() < 0.5 else r2)
        return

    if (len(args) > 0):
        if (args[0] == 'rules'):
            await ctx.send('''Reglas:
1)    La clásica: Respete para que lo respeten
2)   Respeta los canales, el server esta organizado de una manera y ojala sigan ese orden. Si te equivocas de canal borra el mensaje y corrige el error todos cometemos errores pero no postees cosas por donde no van pls

Importante:
#general Aquí pueden hablar de lo que quieran, pero no hagan spam pls para eso esta el "pa-levelear"
#memes Aquí pueden compartir sus memazos de cualquier categoría
#musiquita Canal designado para pedir musiquita
#sugerencias Canal para enviar sugerencias para el server, se aceptan emotes, cabe destacar que no todas las sugerencias serán aceptadas. Si su comentario no contribuye a la sugerencia absténgase de comentar pls
#reclamos Aquí pueden dejar sus reclamos del servidor, por favor sean bien claros del porque y si pueden dar una solución mejor, no se aceptaran reclamos por interno.
#pa-levelear Aquí pueden hacer todo el spam que quieran para levelear el mee6

De cada categoría de juegos
#general Es para que compartan sus nicks por allí y hablen de dicho juego por allí, en el general común se pierden sus mensajes :c''')

    paqueo = random.choice(paqueosPool)
    await ctx.send(paqueo)

# @tasks.loop(seconds=60)
# async def irAPaquear():
#     randomKey = random.choice(list(canales.keys()))
#     print('move to:', randomKey)
#     await connectToVoiceChannel()

async def irAPaquear():
    while True:
        randomKey = random.choice(list(canales.keys()))
        print('move to:', randomKey)
        await connectToVoiceChannel(randomKey)
        await asyncio.sleep(60*5)


async def connectToVoiceChannel(key):
    if key in canales:
        if len(bot.voice_clients) > 0:
            await bot.voice_clients[0].disconnect()
        channelId = canales[key]
        print(type(channelId), channelId)   
        channel = bot.get_channel(channelId)
        try:
            await channel.connect()
        except:
            print("error")


bot.run('Aqui va el token')