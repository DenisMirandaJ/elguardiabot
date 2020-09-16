# -*- coding: utf8 -*-
import random

from discord.ext import commands
from irAPaquear import IrAPaquearCog
from log import Log
from valores import ENVIRONMENT_LOCAL, Valores

# Valores.TEST=True
Valores.ENVIRONMENT = ENVIRONMENT_LOCAL
bot = commands.Bot(command_prefix=Valores.COMMAND_PREFIX)
Valores.BOT = bot
log = Log()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    bot.server = bot.get_guild(Valores.SERVER_ID())
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
            await ctx.send(paqueado + ' ' + random.choice(Valores.paqueos_por_mencion()))
        return
    paqueo = random.choice(Valores.paqueos_genericos())
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
            await ctx.send(Valores.reglas())
            return
    paqueo = random.choice(Valores.paqueos_genericos())
    await ctx.send(paqueo)
    return


bot.add_cog(IrAPaquearCog(bot))
bot.run(Valores.TOKEN())
