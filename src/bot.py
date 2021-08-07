import logging
from discord.ext import commands
from discord.ext.commands import Bot

logging.basicConfig(level=logging.INFO)

with open("../.token.txt") as file:
    TOKEN = file.read()

bot = Bot(command_prefix="Iroh ")
bot.load_extension("cogs.general")


@bot.command(aliases=["rl", ])
@commands.is_owner()
async def reload(ctx):
    bot.unload_extension("cogs.general")
    bot.load_extension("cogs.general")
    await ctx.send("Reloaded!")


@bot.event
async def on_command(ctx: commands.Context):
    logging.INFO(f"{ctx.author.id} aka {ctx.author.name}: {ctx.command}")
    await ctx.message.delete()


@bot.event
async def on_ready():
    print("READY")


bot.run(TOKEN)
