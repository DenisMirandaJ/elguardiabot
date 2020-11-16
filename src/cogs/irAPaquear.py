"""
Componente del bot guardia. Responsable de la tarea del paqueo, conexiones a canales de voz y uso de mensajes de voz
"""
import random
# noinspection PyPackageRequirements
import discord
# noinspection PyPackageRequirements
from discord.ext import commands, tasks

from configs.constants import Constants


class IrAPaquearCog(commands.Cog):
    """
    Clase gestora de la tarea de paqueo
    """

    def __init__(self, bot_1):
        self.bot = bot_1
        self.data = []
        self.ir_a_paquear.start()
        return

    @tasks.loop(seconds=Constants.TIEMPO_ENTRE_PAQUEOS)
    async def ir_a_paquear(self):
        """
        Tarea que realiza el paqueo
        :return: None
        """
        await connection_protocol()
        return

    @ir_a_paquear.before_loop
    async def antes_de_paquear(self):
        """
        Prambulo de la tarea, espera a que el bot esté listo para conectarse
        :return: None
        """
        await self.bot.wait_until_ready()
        return


async def connection_protocol():
    """
    Procedimiento que intenta conectarse a un canal de voz aleatorio y en caso de hayar 3 o mas usuarios en el al
    momento de la conexion, reproduce un mensaje de voz
    :return: None
    """
    channel = choose_random_channel()
    while not channel:
        channel = choose_random_channel()
    await disconnect_other_voice_clients()
    await connect_to_voice_channel(channel)
    return


def is_excluded_channel(random_voice_channel):
    """
    Procedimiento que varifica que un canal no esté excluido
    :param random_voice_channel:
    :return: True si está excluido. False de otra manera.
    """
    if random_voice_channel.id in Constants.excluded_channels.values():
        return True
    return False


def choose_random_channel():
    """
    Función que intenta obtener un canal de voz habil.
    :return: random_voice_channel en exito. None de otra forma.
    """
    random_voice_channel = get_random_channel()
    if is_excluded_channel(random_voice_channel) is True:
        return None
    if has_required_people(random_voice_channel) is False:
        return None
    if has_perm_to_connect(random_voice_channel) is False:
        return None
    if bot_has_connected_clients():
        if random_channel_is_connected_one(random_voice_channel):
            return None
    return random_voice_channel


def random_channel_is_connected_one(voice_channel):
    """
    Función booleana que indica si el canal voice_channel es el canal al que está conectado el cliente del bot
    :param voice_channel: canal a verificar
    :return: boolean
    """
    return voice_channel == Constants.BOT.voice_clients[0].channel


def has_required_people(voice_channel):
    """
    Función booleana que indica si en el canal voice_channel está la cantidad requerida de clientes de voz
    :param voice_channel:
    :return: boolean
    """
    return len(voice_channel.members) == 0 or len(voice_channel.members) >= Constants.cantidadMinParaPaquear


def has_perm_to_connect(voice_channel):
    """
    Función que verifica si el BOT no tiene prohibido conectarse voice_channel
    :param voice_channel:
    :return: True, si lo tiene explicitamente permitido.False, si lo tiene explicitamente prohibido. None si lo tiene implicitamente permitido
    """
    bot_roles = Constants.BOT.server.me.roles
    for role in voice_channel.overwrites:
        perm_override = voice_channel.overwrites[role]
        if role in bot_roles:
            return perm_override.connect
    return None


def bot_has_connected_clients():
    """
    boolean check if the Bot has voice clients connected
    :return: boolean
    """
    return len(Constants.BOT.voice_clients) > 0


def get_random_channel():
    """
    fetch a random voice channel from the current server
    :return: random_voice_channel {voice_channel}
    """
    voice_channels = Constants.BOT.server.voice_channels
    random_voice_channel = random.choice(voice_channels)
    return random_voice_channel


async def disconnect_other_voice_clients():
    """
    Realiza la desconexion de todos los otros clientes de voz en el momento del bot
    :return: None
    """
    while bot_has_connected_clients():
        for client in Constants.BOT.voice_clients:
            await client.disconnect()
    return


async def connect_to_voice_channel(channel):
    """
    Intenta realizar una conexion a un canal de voz dado, en caso de haber 3 o mas personas conectadas reproduce
    un mensaje
    :param channel:
    :return:
    """
    print("Attempting move to: ", channel)
    await channel.connect()
    if len(channel.members) >= Constants.cantidadMinParaPaquear:
        await fumando()
    await turn_mute(voice_client=Constants.BOT.voice_clients[0], estado=True)
    return


async def turn_mute(voice_client, estado):
    """
    Metodo que alterna el estado de silencio del cliente de voz del bot
    :param voice_client: cliente de voz a modificar
    :param estado: Booleano del estado objetivo
    :return: None
    """
    await voice_client.main_ws.voice_state(guild_id=voice_client.guild.id, channel_id=voice_client.channel.id,
                                           self_mute=estado)
    return


async def fumando():
    """
    Metodo que reproduce en el primer cliente de voz del bot el audio "tan_fumando_senore.mp3"
    :return: None
    """
    voice_client = Constants.BOT.voice_clients[0]
    voice_channel = voice_client.channel
    if voice_channel is not None:
        audio = Constants.PATH_SOURCES + "tan_fumando_senore.mp3"
        voice_client.play(discord.FFmpegPCMAudio(executable=Constants.PATH_FFMPEG, source=audio))
    return
