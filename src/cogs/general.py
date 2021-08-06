import datetime
import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def echo(self,ctx: commands.Context):
        await ctx.send(f"{ctx.author} said {ctx.message.content}")

    @commands.command()
    async def info(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Info about Iroh",
            description="very much WIP"
        )
        embed.add_field(name="Author", value="<@!291291715598286848>")
        embed.add_field(name="Source", value="naw, not yet")
        embed.set_author(
            name=ctx.author.name,
            icon_url=ctx.author.avatar_url,
        )
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def test(self, ctx: commands.Context):
        """
        Test command
        """
        await ctx.send("test!")


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))
