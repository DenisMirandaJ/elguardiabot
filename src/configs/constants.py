# -*- coding: utf8 -*-
from configs import botTokens

# MAGIC CONSTANTS
ENVIRONMENT_SERVER = 0
ENVIRONMENT_LOCAL = 1

# Settings
VERSION = None
TIEMPO_ENTRE_PAQUEOS = 60  # default:60f
cantidadMinParaPaquear = 5  # default:5
COMMAND_PREFIX = '-'
BOT = None

# ids
server_id = None
token = None

# messages
HELP_STRING = 'Vaya a http://54.232.65.234:8000/ aún tenemos pendiente el dominio'
paqueos_genericos = None
paqueos_por_mencion = None
reglas = None

# paths
PATH_SOURCES = ''
PATH_FFMPEG = ''
PATH_LOGS = ''


def gen_paqueos_genericos():
    paqueo1 = 'a ver muestrenme sus credenciales'
    paqueo2 = '\*foto a la credencial\* esto le va a llegar a su jefe de carrera'
    paqueo3 = 'ya chicos retirense'
    paqueo4 = '\*Por la radio\* atención, hay un grupo sospechoso en los pastos'
    paqueo5 = 'Creen que soy wn, que no me doy cuenta lo que hacen'
    paqueo6 = 'tenemos un 3312'
    paqueo7 = 'Ya chicos, se puede estar dentro de la universidad solo hasta las 9 vayan saliendo'
    return [paqueo1, paqueo2, paqueo3, paqueo4, paqueo5, paqueo6, paqueo7]


def gen_paqueos_por_mencion():
    paqueo1 = 'muestreme su credencial'
    paqueo2 = 'apague eso, no se puede fumar acá'
    paqueo3 = ' cortese el pelo'
    return [paqueo1, paqueo2, paqueo3]


def gen_reglas():
    texto = '''Reglas:
        1)    La clásica: Respete para que lo respeten
        2)   Respeta los canales, el server esta organizado de una manera y ojalá sigan ese orden. Si te equivocas de canal borra el mensaje y corrige el error todos cometemos errores pero no postees cosas por donde no van pls

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


def startup(environment=ENVIRONMENT_SERVER, test=False):
    if environment is ENVIRONMENT_SERVER:
        super().PATH_SOURCES = '/home/ubuntu/elguardiabot/res/'
        super().PATH_FFMPEG = PATH_SOURCES + '/ffmpeg/ffmpeg'
        super().PATH_LOGS = '/home/ubuntu/elguardiabot/logs/'
    elif environment is ENVIRONMENT_LOCAL:
        super().PATH_SOURCES = '../res/'
        super().PATH_FFMPEG = PATH_SOURCES + 'ffmpeg/ffmpeg.exe'
        super().PATH_LOGS = '../logs/'
    if test is True:
        super().server_id = 760614553636962304
        super().token = botTokens.protoToken
    elif test is False:
        super().server_id = 702167240463876129
        super().token = botTokens.tokenGuardia
    super().paqueos_genericos = gen_paqueos_genericos()
    super().paqueos_por_mencion = gen_paqueos_por_mencion()
    super().reglas = gen_reglas()
