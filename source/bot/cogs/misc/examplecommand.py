import discord
from discord.ext import commands
from source.bot.utils import BaseEmbed
from inspect import getmembers, isclass
from sys import modules
class ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await BaseEmbed(ctx, 'Hola', f'A hola message.')

async def setup(client):
    classes = getmembers(modules[__name__], isclass)
    main_class = classes[0][1]
    await client.add_cog(main_class(client))