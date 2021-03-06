# -*- coding: utf8 -*-
import random

import discord

from discord.ext import commands, tasks
from valores import ENVIRONMENT_LOCAL, Valores

valores = Valores(test=False, environment=ENVIRONMENT_LOCAL)

bot = commands.Bot(command_prefix=valores.COMMAND_PREFIX)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    bot.server = bot.get_guild(valores.SERVER_ID)
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
            await ctx.send(paqueado + ' ' + random.choice(valores.pool_paqueos_mencion()))
        return
    paqueo = random.choice(valores.pool_paqueos_genericos())
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
            await ctx.send(valores.reglas())
            return
    paqueo = random.choice(valores.pool_paqueos_genericos())
    await ctx.send(paqueo)
    return


class IrAPaquearCog(commands.Cog):
    def __init__(self, bot_1):
        self.bot = bot_1
        self.data = []
        self.irAPaquear.start()
        return

    @tasks.loop(seconds=valores.TIEMPO_ENTRE_PAQUEOS)
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
    await disconnectOtherVoiceClients()
    await connectToVoiceChannel(channel)
    return


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


async def disconnectOtherVoiceClients():
    while len(bot.voice_clients) > 0:
        for client in bot.voice_clients:
            await client.disconnect()
    return


async def connectToVoiceChannel(channel):
    print("Attempting move to: ", channel)
    await channel.connect()
    if len(channel.members) >= 3:
        await fumando()
    await selfMute(bot.voice_clients[0])
    return


async def selfMute(voiceClient):
    await voiceClient.main_ws.voice_state(guild_id=voiceClient.guild.id, channel_id=voiceClient.channel.id,
                                          self_mute=True)
    return


async def unMute(voiceClient):
    await voiceClient.main_ws.voice_state(guild_id=voiceClient.guild.id, channel_id=voiceClient.channel.id,
                                          self_mute=False)
    return


async def fumando():
    voiceClient = bot.voice_clients[0]
    voiceChannel = voiceClient.channel
    if voiceChannel is not None:
        audio = valores.PATH_SOURCES + "tan_fumando_senore.mp3"
        voiceClient.play(discord.FFmpegPCMAudio(executable=valores.PATH_FFMPEG, source=audio))
    return


bot.add_cog(IrAPaquearCog(bot))
bot.run(valores.TOKEN)
