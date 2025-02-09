import discord
from discord.ext import commands

# Definindo o prefixo e o canal de texto
prefixo = "!!"  # Você pode mudar o prefixo para o que quiser
canal_id = 1338130998071787592  # Substitua com o ID do canal de texto onde o bot vai responder

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True  # Permissão para ler conteúdo das mensagens

bot = commands.Bot(command_prefix=prefixo, intents=intents)

# Evento quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f'{bot.user} está conectado!')

# Comando simples para responder a uma mensagem
@bot.command()
async def hello(ctx):
    # Verifica se a mensagem foi enviada no canal correto
    if ctx.channel.id == canal_id:
        await ctx.send(f"Olá, {ctx.author.mention}! Eu sou um bot!")

# Rodando o bot com o token
bot.run('d3ea434cc06284a4aa02bbd6e231fb70cd379adec8e6730c8e24b25e3b0d2477')  # Substitua 'seu_token_aqui' pelo seu token de bot
