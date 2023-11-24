import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я Диалоговый Бот!')

@bot.command()
async def help(ctx):
    await ctx.send(f'Я имею команды:
                   Диалоговые:
                   1)h.a.y-спрашивание как дела
                   2)w.y.s.m.a.s-советует один сервер
                   3)wahtdoyodo?-спрашивание что делаешь
                   Советные(советы по теме глобального потепления):
                   1)w.t.d.i.i.s.t-что делать если увидел мусор
                   2)stop.glob.warm-как остановить потепление
                   Приятного использованию Диалоговым ботом:)')

bot.run("token")
