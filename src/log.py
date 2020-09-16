"""
Componente del bot guardia. Responsable de generar los archivos de registro del bot
"""
import logging
from datetime import datetime

from valores import Valores


class Log:
    """
    Clase encargada de generar los archivos de registo
    """
    def __init__(self):
        logger = logging.getLogger('discord')
        logger.setLevel(logging.DEBUG)
        file_name = datetime.now().strftime('log_%Y_%m_%d_%H_%M.log')
        handler = logging.FileHandler(filename=Valores.PATH_LOGS + file_name, encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)
