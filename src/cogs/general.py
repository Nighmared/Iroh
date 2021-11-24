import datetime

import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord_components import Button, DiscordComponents


class General(commands.Cog):

    EXTENSIONS = ("cogs.quotes",)

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        DiscordComponents(self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.load_extensions()

    async def load_extensions(self):
        for ext in self.EXTENSIONS:
            try:
                self.bot.load_extension(ext)
            except discord.ext.commands.errors.ExtensionAlreadyLoaded:
                continue

    async def reload_cog(self, cog: str):
        self.bot.reload_extension(f"cogs.{cog.lower()}")
        return True
        print(str(e))
        return False

    @commands.command(
        aliases=[
            "rl",
        ]
    )
    @commands.is_owner()
    async def reload(self, ctx: Context, cog: str = None):
        """
        reload a specific cog or all of them.
        """
        if cog is None:
            reloaded_cogs = []
            cogs = self.bot.cogs.copy().keys()
            for c in cogs:
                if await self.reload_cog(c):
                    reloaded_cogs.append(c)
            res = "Reloaded Cogs:\n-" + "\n-".join(reloaded_cogs)
        else:
            cog = cog.lower()
            if cog in map(lambda x: x.lower(), self.bot.cogs.keys()):
                await self.reload_cog(cog)
                res = f"Reloaded {cog}"
            else:
                res = "Invalid cog name! Valid cogs are:\n " + ", ".join(self.bot.cogs)
        embed = discord.Embed(title="Reload", description=res)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx: Context, *words):
        """
        says whatever comes after the command
        """
        if len(words) == 0:
            return
        msg = await ctx.send("TBA")
        await msg.edit(
            content="Saying «"
            + " ".join(words)
            + f"»\n at the request of {ctx.author.name}"
        )

    @commands.command(
        aliases=[
            "d",
        ]
    )
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
        embed.set_image(
            url="https://repository-images.githubusercontent.com/393521076/b45b0860-a02b-4ba9-8d79-f588e9ea7b2b"
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
        interaction = await self.bot.wait_for(
            "button_click", check=lambda i: i.component.label.startswith("DANG")
        )
        await msg.delete()
        await interaction.respond(content="HELO")


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))
