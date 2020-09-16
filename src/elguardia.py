# -*- coding: utf8 -*-
"""
Bot de guardia, este archivo contiene los comandos es su inicializador
"""
import random

from discord.ext import commands
from irAPaquear import IrAPaquearCog
from log import Log
# noinspection PyUnresolvedReferences
from valores import ENVIRONMENT_LOCAL, Valores

####
# VERSION
Valores.VERSION = "1.0.0.0"
####


# Valores.TEST=True
# Valores.ENVIRONMENT = ENVIRONMENT_LOCAL
bot = commands.Bot(command_prefix=Valores.COMMAND_PREFIX)
Valores.BOT = bot
log = Log()


@bot.event
async def on_ready():
    """
    Evento disparado al estar listo el bot, entrega información breve y obtiene el servidor de conexión
    :return: None
    """
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    bot.server = bot.get_guild(Valores.SERVER_ID())
    print('------')
    return


@bot.command()
async def paquear(ctx, *args):
    """
    Comando de paqueo, soporta etiquetas
    :param ctx: Contexto
    :param args: Estamentos tras el comando, separados por espacios
    :return: None
    """
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
            await ctx.send(paqueado + ' ' + random.choice(Valores.paqueos_por_mencion()))
        return
    paqueo = random.choice(Valores.paqueos_genericos())
    await ctx.send(paqueo)
    return


@bot.command()
async def guardia(ctx, *args):
    """
    Comando general del bot, soporta instrucciones de [dar <str>], [rules] y [version!]
    :param ctx: Contexto
    :param args: Estamentos tras el comando, separados por espacios
    :return: None
    """
    print('guardia')
    if len(args) == 2 and args[0] == 'dar':
        r1 = '\*Se come el {}\* Gracias estaba muy bueno'.format(args[1])
        r2 = 'No gracias, no como en el trabajo'
        await ctx.send(r1 if random.random() < 0.5 else r2)
        return
    if len(args) == 1:
        if args[0] == 'rules':
            await ctx.send(Valores.reglas())
            return
        if args[0] == "version!":
            ctx.send(Valores.VERSION)
    return


bot.add_cog(IrAPaquearCog(bot))
bot.run(Valores.TOKEN())
