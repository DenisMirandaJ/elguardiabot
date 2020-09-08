# -*- coding: utf8 -*-

import asyncio
import random

from discord.ext import commands

import contants


currentChanel = None
command_prefix = '-'
bot = commands.Bot(command_prefix)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.loop.create_task(irAPaquear())


@bot.command()
async def paquear(ctx, *args):
    if len(args) == 1:
        if args[0].lower() == 'guetti':
            await ctx.send('Guetti deja el lol')
            return
        if args[0].lower() == 'lixo':
            await ctx.send('Cortese el pelo jipy')
            return
        if args[0].lower() == 'denis':
            await ctx.send('deja de estar sad ;c')
            return
        if len(ctx.message.mentions) == 1:
            paqueado = ctx.message.mentions[0].mention
            await ctx.send(paqueado + ' ' + random.choice(contants.paqueosPorMencion))
        await connectToVoiceChannel(args[0])
        return
    paqueo = random.choice(contants.paqueosPool)
    await ctx.send(paqueo)


@bot.command()
async def guardia(ctx, *args):
    print('guardia')
    if len(args) == 2 and args[0] == 'dar':
        r1 = '\*Se come el {}\* Gracias estaba muy bueno'.format(args[1])
        r2 = 'No gracias, no como en el trabajo'
        await ctx.send(r1 if random.random() < 0.5 else r2)
        return

    if len(args) > 0:
        if args[0] == 'rules':
            await ctx.send(contants.reglas)

    paqueo = random.choice(contants.paqueosPool)
    await ctx.send(paqueo)


# @tasks.loop(seconds=60)
# async def irAPaquear():
#     randomKey = random.choice(list(canales.keys()))
#     print('move to:', randomKey)
#     await connectToVoiceChannel()

async def irAPaquear():
    while True:
        randomKey = random.choice(list(contants.canales.keys()))
        print('move to:', randomKey)
        await connectToVoiceChannel(randomKey)
        await asyncio.sleep(60 * 5)


async def connectToVoiceChannel(key):
    if key in contants.canales:
        if len(bot.voice_clients) > 0:
            await bot.voice_clients[0].disconnect()
        channelId = contants.canales[key]
        print(type(channelId), channelId)
        channel = bot.get_channel(channelId)
        try:
            await channel.connect()
        except:
            print("error")

bot.run(contants.protoToken)
