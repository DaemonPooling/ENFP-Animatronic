import os
import sys
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
project_root = os.getenv('PROJECT_ROOT')
sys.path.insert(0, project_root)
from source.data.db import supabase  # Knowing that db.py is in the source/data directory
from source.bot.utils import CogAlert, BaseEmbed, RaiseDBError
from inspect import getmembers, isclass
from sys import modules

class ForgetBirthday(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def forgetbirthday(self, ctx):
        try:
            user_id = str(ctx.author.id)
            result = supabase.table("birthdays").delete().eq('user_id', user_id).execute()
            if result:
                await BaseEmbed(ctx, 'Forgot birthday', f'Your birthday is removed!')
                CogAlert(ctx.author.name)
        except Exception as e:
            await RaiseDBError(ctx, e)
            
async def setup(client):
    classes = getmembers(modules[__name__], isclass)
    main_class = classes[0][1]
    await client.add_cog(main_class(client))
