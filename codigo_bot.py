import discord
import random
from urllib.parse import quote_plus
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)


class Google(discord.ui.View):
    def __init__(self, query: str):
        super().__init__()

        query = quote_plus(query)
        url = f'https://www.google.com/search?q={query}'

        self.add_item(discord.ui.Button(label="Pesquisar no Google 🔎", url=url))
# -------- Funções --------

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)

def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "cara"
    else:
        return "coroa"


# -------- Eventos --------

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')
    print('---------------------------------------')


# -------- Comandos --------

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! Eu sou um bot {bot.user}!')


@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def senha(ctx):
    await ctx.send(gen_pass(10))


@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emoji())


@bot.command()
async def moeda(ctx):
    await ctx.send(flip_coin())


@bot.command()
async def entrada(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} entrou {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def google(ctx, *, pesquisa: str):
    await ctx.send(f'Resultado da busca para: `{pesquisa}`', view=Google(pesquisa))

    
bot.run(SEU TOKEN)
