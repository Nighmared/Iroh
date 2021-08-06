from discord.ext import commands
from discord.ext.commands import Bot


with open("../.token.txt") as file:
    TOKEN = file.read()

bot = Bot(command_prefix="!!")
bot.load_extension("cogs.general")


@bot.command()
@commands.is_owner()
async def reload(ctx):
    bot.unload_extension("cogs.general")
    bot.load_extension("cogs.general")
    await ctx.send("Reloaded!")

@bot.event
async def on_command(ctx):
    await ctx.message.delete()

bot.run(TOKEN)
