# -*- coding: utf8 -*-

import random
import traceback

from discord.ext import commands, tasks

import botTokens
import valores

bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


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
        await connectToVoiceChannel(args[0])
        return
    paqueo = random.choice(valores.paqueosPool)
    await ctx.send(paqueo)


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


class IrAPaquearCog(commands.Cog):
    def __init__(self, bot_1):
        self.bot = bot_1
        self.data = []
        self.irAPaquear.start()

    @tasks.loop(seconds=60)
    async def irAPaquear(self):
        randomKey = random.choice(list(valores.canales.keys()))
        print('move to:', randomKey)
        await connectToVoiceChannel(randomKey)

    @irAPaquear.before_loop
    async def beforePaquear(self):
        await self.bot.wait_until_ready()


async def connectToVoiceChannel(key):
    if key in valores.canales:
        if len(bot.voice_clients) > 0:
            await bot.voice_clients[0].disconnect()
        channelId = valores.canales[key]
        print(type(channelId), channelId)
        channel = bot.get_channel(channelId)
        if channel is None:
            return
        try:
            await channel.connect()
        except Exception as e:
            print("error")
            traceback.print_exc(e)


@bot.command()
async def mandarAPaquear(ctx):
    randomVoiceChannel = random.choice(ctx.guild.voice_channels)
    if len(ctx.bot.voice_clients) > 0:
        while randomVoiceChannel == ctx.bot.voice_clients[0].channel:
            randomVoiceChannel = random.choice(ctx.guild.voice_channels)
        await ctx.bot.voice_clients[0].disconnect()
    print("Attempting to move to: ", randomVoiceChannel)
    await randomVoiceChannel.connect()
    return


bot.add_cog(IrAPaquearCog(bot))
bot.run(botTokens.protoToken)
