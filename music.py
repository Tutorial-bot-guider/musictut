import discord 
from discord.ext import commands
import random


TOKEN = 'NjQ5NDgyNTA0NzYzNjA0OTky.Xd9fqA.hTGhXt8fmwZ-1jkRckfsFkgdsbQ'

bot = commands.Bot(command_prefix = '!')
bot.remove_command('help')

players = {}

@bot.event
async def on_ready():
    print('XAMAAAAAAAA')

@bot.command(pass_context=True)
async def vaza(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()

@bot.command(pass_context=True)
async def chama(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player('https://www.youtube.com/watch?v=V_rWYRY-pOs')
    players[server.id] = player
    player.start()

@bot.command(pass_context=True)
async def melhorcoisadomundo(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player('https://www.youtube.com/watch?v=HTrB4i1MbNQ')
    players[server.id] = player
    player.start()

@bot.command(pass_context=True)
async def levantate(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player('https://www.youtube.com/watch?v=rF7lhBnYXn4')
    players[server.id] = player
    player.start()

@bot.command(pass_context=True)
async def pera(ctx):
    id = ctx.message.server.id
    players[id].pause()

@bot.command(pass_context=True)
async def para(ctx):
    id = ctx.message.server.id
    players[id].stop()

@bot.command(pass_context=True)
async def bora(ctx):
    id = ctx.message.server.id
    players[id].resume()

@bot.command(pass_context=True)
async def moita(ctx):
    await ctx.send("o Moita é o cara!")

@bot.command(pass_context=True)
async def bomdia(ctx):
    await ctx.send_message("bom dia grupo!")

bot.run(TOKEN)
