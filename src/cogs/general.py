import datetime
import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord_components import DiscordComponents, Button

class General(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        DiscordComponents(self.bot)

    @commands.command()
    async def say(self, ctx: Context, *words):
        """
        says whatever comes after the command
        """
        if len(words) == 0:
            return
        await ctx.send("Saying "+" ".join(words) + f"\n at the request of {ctx.author.name}")

    @commands.command(aliases=['d',])
    @commands.is_owner()
    async def delete(self, ctx: commands.Context):
        """
        Deletes message that is replied to
        Owner only
        """
        to_delete_id = ctx.message.reference.message_id
        to_delete_chan_id = ctx.message.reference.channel_id
        to_delete_chan = await self.bot.fetch_channel(to_delete_chan_id)
        to_delete = await to_delete_chan.fetch_message(to_delete_id)
        await to_delete.delete()

    @commands.command()
    async def info(self, ctx: Context):
        """
        Basic info about the bot
        """
        embed = discord.Embed(
            title="Info about Iroh",
            description="very much WIP",
            url="https://github.com/Nighmared/Iroh",
        )
        embed.set_image(url="https://repository-images.githubusercontent.com/393521076/b45b0860-a02b-4ba9-8d79-f588e9ea7b2b"
)
        embed.add_field(name="Author", value="<@!291291715598286848>")
        embed.add_field(name="Source", value="https://github.com/Nighmared/Iroh")
        embed.set_author(
            name=ctx.author.name,
            icon_url=ctx.author.avatar_url,
        )
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def button(self, ctx):
        """
        sends a button. much wow.

        never gonna give you up, never gonna let you down <3
        """
        msg = await ctx.send(
            "does this have a button?",
            components=[
                Button(label="DANG"),
            ],
        )
        interaction = await self.bot.wait_for("button_click", check=lambda i:i.component.label.startswith("DANG"))
        await msg.delete()
        await interaction.respond(content="HELO")


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))
