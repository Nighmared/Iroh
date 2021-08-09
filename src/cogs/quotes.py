from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context
from random import choice
import json

class Quotes(commands.Cog):
    def __init__(self):
        with open("../data/iroh_quotes.json",'r') as f:
            self.quotes = json.load(f)['quotes']

    @commands.command()
    async def quote(self, ctx:Context, category:str ="sweet"):
        """
        Sends a quote by the infinitely wise Uncle Iroh.
        Default category is 'sweet', the other available option is 'fun'
        """
        if not category.lower() in ("fun", "sweet"):
            category = "sweet"

        to_send = choice(self.quotes[category])
        embed = Embed(title="Uncle Iroh Quotes", description=to_send)
        embed.set_author(name=ctx.author)
        embed.set_author(
            name=ctx.author.name,
            icon_url=ctx.author.avatar_url,
        )
        embed.set_image(url="https://repository-images.githubusercontent.com/393521076/b45b0860-a02b-4ba9-8d79-f588e9ea7b2b")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Quotes())
