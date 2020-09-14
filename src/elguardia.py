# -*- coding: utf8 -*-

import random

from discord.ext import commands, tasks
from discord.utils import deprecated

import botTokens
import valores

bot = commands.Bot(command_prefix='-')
token = botTokens.tokenGuardia
serverDePaqueo = valores.serverId


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    bot.server = bot.get_guild(serverDePaqueo)
    print('------')
    return


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
            await ctx.send(paqueado + ' ' + random.choice(valores.paqueosPorMencion))
        return
    paqueo = random.choice(valores.paqueosPool)
    await ctx.send(paqueo)
    return


@bot.command()
async def guardia(ctx, *args):
    print('guardia')
    if len(args) == 2 and args[0] == 'dar':
        r1 = '\*Se come el {}\* Gracias estaba muy bueno'.format(args[1])
        r2 = 'No gracias, no como en el trabajo'
        await ctx.send(r1 if random.random() < 0.5 else r2)
        return
    if len(args) == 1:
        if args[0] == 'rules':
            await ctx.send(valores.reglas)
            return
    paqueo = random.choice(valores.paqueosPool)
    await ctx.send(paqueo)
    return


class IrAPaquearCog(commands.Cog):
    def __init__(self, bot_1):
        self.bot = bot_1
        self.data = []
        self.irAPaquear.start()
        return

    @tasks.loop(seconds=60)
    async def irAPaquear(self):
        await connectionProtocol()
        return

    @irAPaquear.before_loop
    async def beforePaquear(self):
        await self.bot.wait_until_ready()
        return


async def connectionProtocol():
    channel = chooseRandomChannel()
    while not channel:
        channel = chooseRandomChannel()
    await disconnectOthers()
    await connectToVoiceChannel(channel)


# noinspection PyUnresolvedReferences
def chooseRandomChannel():
    randomVoiceChannel = random.choice(bot.server.voice_channels)
    canConnect = None
    for role in randomVoiceChannel.overwrites:
        permOverride = randomVoiceChannel.overwrites[role]
        if role.name == "@everyone" or role.name == "uwus":
            canConnect = permOverride.connect
            break
    if canConnect is False:
        return None
    if len(bot.voice_clients) > 0:
        if randomVoiceChannel == bot.voice_clients[0].channel:
            return None
    return randomVoiceChannel


async def disconnectOthers():
    while len(bot.voice_clients) > 0:
        for client in bot.voice_clients:
            await client.disconnect()
    return


async def connectToVoiceChannel(channel):
    print("Attempting to move to: ", channel)
    await channel.connect()
    return


@deprecated
@bot.command()
async def mandarAPaquear():
    await connectionProtocol()
    return


bot.add_cog(IrAPaquearCog(bot))
bot.run(token)
