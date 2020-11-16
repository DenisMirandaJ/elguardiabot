# -*- coding: utf8 -*-
"""
Archivo que define las constantes y configurables del bot
"""
import os

from configs import botTokens

# MAGIC CONSTANTS
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/"
LINUX_amd64 = 1
WIN10_x64 = 2


class Constants:
    """
    Clase estatica que define el comportamiento configurable y constantes a utilizar por el bot
    """

    #
    #
    # -------------------------------------------------
    # Ajustes de IrAPaquear.py
    # -------------------------------------------------
    #
    #
    TIEMPO_ENTRE_PAQUEOS = 3
    """
    Constante que define el periodo de segundos entre rondas te la tarea
    suggested = 60
    """

    cantidadMinParaPaquear = 5
    """
    Constante que define la cantidad minima de clientes de voz conectados a un canal 
    de voz para que sea candidato a la ronda y/o paqueo por voz.
    suggested = 5
    """

    #
    #
    # -------------------------------------------------
    # Mensajes
    # -------------------------------------------------
    #
    #
    HELP_STRING = "No hay ayuda para los vagos, diríjase a https://github.com/vichaoss/elguardiabot e infórmese."
    #   'Vaya a http://54.232.65.234:8000/ aún tenemos pendiente el dominio'
    """
    Mensaje a enviar cuando se realiza el comando '-guardia help'
    """

    paqueos_genericos = None
    """
    Pool de paqueos invocada en '-guardia paquear'. Asignada en startup() via gen_paqueos_genericos()
    """

    paqueos_por_mencion = None
    """
    Pool de paqueos invocada en '-guardia paquear @[etiqueta]'. Asignada en startup() via gen_paqueos_genericos()    
    """

    excluded_channels = None

    reglas = None
    """
    Mensaje a enviar cuando se realiza el comando '-guardia rules'. Asignado en startup() via gen_reglas()
    """

    #
    #
    # -------------------------------------------------
    # Constantes asignadas en función a startup() 'test'
    # -------------------------------------------------
    #
    #
    server_id = None
    """
    Id del servidor con el cual se esteblecerá la conexión.
    """
    token = ''
    """
    Credencial de conexión, asignado en la función startup() en función de 'test'
    """

    #
    #
    # -------------------------------------------------
    # Constantes asignadas en función a startup() 'project_path'
    # -------------------------------------------------
    #
    #
    PATH_SOURCES = ''
    """
    Ruta de los archivos de recursos.
    """
    PATH_FFMPEG = ''
    """
    Ruta de los ejecutables FFMPEG
    """
    PATH_LOGS = ''
    """
    Ruta de los archivos de registro
    """

    #
    #
    # -------------------------------------------------
    # Constantes de información y referencia
    # -------------------------------------------------
    #
    #
    VERSION = None
    """
    Constante que indica la versión actual del bot, asignada al inicio de elguardia.py
    """

    BOT = None
    """
    Constante que referencia al bot que se está ejecutando, asignada en el comienzo de elguardia.py
    """

    COMMAND_PREFIX = '-'
    """
    Prefijo de comandos para invocar al bot.
    """

    @staticmethod
    def startup(operating_system=LINUX_amd64, test=False):
        """
        Metodo estatico que asigna la configuración dinamica del bot, en función a su entorno
        y sea de pruebas o retail, también invoca los metodos generadores de los mensajes
        :param operating_system: Sistema operativo en el que se iniciará el bot
        :param test: booleano, si utiliza o no las credenciales de pruebas
        :return:
        """
        Constants.PATH_SOURCES = PROJECT_PATH + 'res/'
        Constants.PATH_LOGS = PROJECT_PATH + 'logs/'
        if operating_system is LINUX_amd64:
            Constants.PATH_FFMPEG = Constants.PATH_SOURCES + 'ffmpeg/ffmpeg-4.3.1-amd64-static/ffmpeg'
        elif operating_system is WIN10_x64:
            Constants.PATH_FFMPEG = Constants.PATH_SOURCES + 'ffmpeg/ffmpeg.exe'

        if test is True:
            Constants.server_id = 760614553636962304
            Constants.token = botTokens.protoToken
        elif test is False:
            Constants.server_id = 702167240463876129
            Constants.token = botTokens.tokenGuardia

        Constants.excluded_channels = gen_canales_excluidos()
        Constants.paqueos_genericos = gen_paqueos_genericos()
        Constants.paqueos_por_mencion = gen_paqueos_por_mencion()
        Constants.reglas = gen_reglas()
        return


def gen_paqueos_genericos():
    """
    Generador de paqueos genericos
    :return: Lista de strings, donde cada string corresponde a un paqueo
    """
    paqueo1 = 'a ver muestrenme sus credenciales'
    paqueo2 = '\*foto a la credencial\* esto le va a llegar a su jefe de carrera'
    paqueo3 = 'ya chicos retirense'
    paqueo4 = '\*Por la radio\* atención, hay un grupo sospechoso en los pastos'
    paqueo5 = 'Creen que soy wn, que no me doy cuenta lo que hacen'
    paqueo6 = 'tenemos un 3312'
    paqueo7 = 'Ya chicos, se puede estar dentro de la universidad solo hasta las 9 vayan saliendo'
    return [paqueo1, paqueo2, paqueo3, paqueo4, paqueo5, paqueo6, paqueo7]


def gen_paqueos_por_mencion():
    """
    Generador de paqueos por mención
    :return: Lista de strings, donde cada string corresponde a un paqueo
    """
    paqueo1 = 'muestreme su credencial'
    paqueo2 = 'apague eso, no se puede fumar acá'
    paqueo3 = ' cortese el pelo'
    return [paqueo1, paqueo2, paqueo3]


def gen_reglas():
    """
    Generador de las reglas
    :return: String que contiene las reglas
    """
    texto = '''Reglas:
        1) La clásica: Respete para que lo respeten
        2) Respeta los canales, el server esta organizado de una manera y ojalá sigan ese orden. Si te equivocas de canal borra el mensaje y corrige el error todos cometemos errores pero no postees cosas por donde no van pls

        Importante:
        #general Aquí pueden hablar de lo que quieran, pero no hagan spam pls para eso esta el "pa-levelear"
        #memes Aquí pueden compartir sus memazos de cualquier categoría
        #musiquita Canal designado para pedir musiquita
        #sugerencias Canal para enviar sugerencias para el server, se aceptan emotes, cabe destacar que no todas las sugerencias serán aceptadas. Si su comentario no contribuye a la sugerencia absténgase de comentar pls
        #reclamos Aquí pueden dejar sus reclamos del servidor, por favor sean bien claros del porque y si pueden dar una solución mejor, no se aceptarán reclamos por interno.
        #pa-levelear Aquí pueden hacer todo el spam que quieran para levelear el mee6

        De cada categoría de juegos
        #general Es para que compartan sus nicks por allí y hablen de dicho juego por allí, en el general común se pierden sus mensajes :c'''
    return texto


def gen_canales_excluidos():
    """
    Generador de los canales excluidos
    :return: canales excluidos
    """
    canales_excluidos = {"cinema gei": 709250093173178378,

                         }

    return canales_excluidos
