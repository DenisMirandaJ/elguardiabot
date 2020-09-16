# -*- coding: utf8 -*-
import botTokens

ENVIRONMENT_SERVER = 0
ENVIRONMENT_LOCAL = 1


class Valores:

    def __init__(self, test, environment):
        self.PATH_SOURCES = '../res/'
        self.COMMAND_PREFIX = '-'
        # valor deseado = 60f
        self.TIEMPO_ENTRE_PAQUEOS = 5
        if environment is ENVIRONMENT_SERVER:
            self.PATH_FFMPEG = '/usr/bin/ffmpeg'
        if environment is ENVIRONMENT_LOCAL:
            self.PATH_FFMPEG = 'C:/Users/Vichaoss/Downloads/ffmpeg/bin/ffmpeg.exe'
        if test is True:
            self.TOKEN = botTokens.protoToken
            self.SERVER_ID = 752649753430589591
        if test is False:
            self.TOKEN = botTokens.tokenGuardia
            self.SERVER_ID = 702167240463876129

    @staticmethod
    def pool_paqueos_genericos():
        paqueo1 = 'a ver muestrenme sus credenciales'
        paqueo2 = '\*foto a la credencial\* esto le va a llegar a su jefe de carrera'
        paqueo3 = 'ya chicos retirense'
        paqueo4 = '\*Por la radio\* atención, hay un grupo sospechoso en los pastos'
        paqueo5 = 'Creen que soy wn, que no me doy cuenta lo que hacen'
        paqueo6 = 'tenemos un 3312'
        paqueo7 = 'Ya chicos, se puede estar dentro de la universidad solo hasta las 9 vayan saliendo'
        return [paqueo1, paqueo2, paqueo3, paqueo4, paqueo5, paqueo6, paqueo7]

    @staticmethod
    def pool_paqueos_mencion():
        paqueo1 = 'muestreme su credencial'
        paqueo2 = 'apague eso, no se puede fumar acá'
        paqueo3 = ' cortese el pelo'
        return [paqueo1, paqueo2, paqueo3]

    @staticmethod
    def reglas():
        reglas = '''Reglas:
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
        return reglas
