import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yaptık")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Merhaba {bot.user}! Ben bir botum!")
def calender(year):
    if year < 2022:
        return 0
    else:
        total = 8300 * (year - 2022)
        return total

@bot.command()
async def TaylorSwiftCO2(ctx,year:int):
    Jaysus = calender(year)
    await ctx.send(f"Her private jet usage will have amounted to an estimated {Jaysus} tonnes of carbon emissions by {year}")

@bot.command(name='Why should I care about global warming?')
async def WhyshouldIcareaboutglobalwarming(ctx):
    await ctx.send("Because you'll die, idiot.")


bot.run("")
