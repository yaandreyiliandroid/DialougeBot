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
async def info(ctx):
    await ctx.send(f'''hay-как дела?
                        hello-привет
                        goodbye-пока
                        wwyd-что ты будешь делать?
                        isawtrsh-расказывает что делать если увидел мусор
                        stpgp-советы при глобальном потеплении
                        mem-мемчик''')

@bot.command()
async def hay(ctx):
    await ctx.send(f'норм с тобой общаюсь')

@bot.command()
async def goodbye(ctx):
    await ctx.send(f'Пока')

@bot.command()
async def wwyd(ctx):
    await ctx.send(f'пока планов нету')

@bot.command()
async def isawtrsh(ctx):
    await ctx.send(f'для начала наденьте перчатки.Потом сложите мусор в пакет/пакеты из под мусора(желательно рассортировать).И выкиньте его либо в распределёный выброс мусора(желательно так) или в ближайщий мусоропровод')

@bot.command()
async def stpgp(ctx):
    await ctx.send(f'Мои советы:Не разбрасывайте мусор куда не поподя.Страйтесь пользоваться велосипедом или эко-мобилем')

@bot.command()
async def mystery(ctx):
    await ctx.send(f'Пасхалка!')

@bot.command()
async def эээ(ctx):
    await ctx.send(f'Пасхалка! на русском')
    images = os.listdir('lol')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Привет {member.mention} Добро пожаловать в {guild.name}! Я диалоговый бот! напиши команду $info чтобы узнать какие команды уменя есть'
            await guild.system_channel.send(to_send)

#выдача секретной роли
@bot.command()
async def hidenrole(ctx):
    await ctx.send(f'мама мия да это же Секретная роль!!!!')
    author = ctx.message.author
    guild = bot.get_guild(1109383919079542784)
    role = guild.get_role(1181266780124098651)

    await author.add_roles(role)



intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)

bot.run("token")
