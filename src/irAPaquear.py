import random

import discord
from discord.ext import commands, tasks
from valores import Valores


class IrAPaquearCog(commands.Cog):
    def __init__(self, bot_1):
        self.bot = bot_1
        self.data = []
        self.irAPaquear.start()
        return

    @tasks.loop(seconds=Valores.TIEMPO_ENTRE_PAQUEOS)
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


def chooseRandomChannel():
    randomVoiceChannel = random.choice(Valores.BOT.server.voice_channels)
    canConnect = None
    for role in randomVoiceChannel.overwrites:
        permOverride = randomVoiceChannel.overwrites[role]
        if role.name == "@everyone" or role.name == "uwus":
            canConnect = permOverride.connect
            break
    if canConnect is False:
        return None
    if len(Valores.BOT.voice_clients) > 0:
        if randomVoiceChannel == Valores.BOT.voice_clients[0].channel:
            return None
    return randomVoiceChannel


async def disconnectOtherVoiceClients():
    while len(Valores.BOT.voice_clients) > 0:
        for client in Valores.BOT.voice_clients:
            await client.disconnect()
    return


async def connectToVoiceChannel(channel):
    print("Attempting move to: ", channel)
    await channel.connect()
    if len(channel.members) >= 3:
        await fumando()
    await selfMute(Valores.BOT.voice_clients[0])
    return


async def selfMute(voiceClient):
    await voiceClient.main_ws.voice_state(guild_id=voiceClient.guild.id, channel_id=voiceClient.channel.id,
                                          self_mute=True)
    return


async def unMute(voiceClient):
    await voiceClient.main_ws.voice_state(guild_id=voiceClient.guild.id, channel_id=voiceClient.channel.id,
                                          self_mute=False)
    return


# Metodo que reproduce en el primer cliente de voz del bot el audio "tan_fumando_senore.mp3"
async def fumando():
    voiceClient = Valores.BOT.voice_clients[0]
    voiceChannel = voiceClient.channel
    if voiceChannel is not None:
        audio = Valores.PATH_SOURCES + "tan_fumando_senore.mp3"
        voiceClient.play(discord.FFmpegPCMAudio(executable=Valores.PATH_FFMPEG(), source=audio))
    return
