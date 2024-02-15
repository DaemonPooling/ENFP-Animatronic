import os
import sys
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
project_root = os.getenv('PROJECT_ROOT')
sys.path.insert(0, project_root)
from source.data.db import supabase  # Knowing that db.py is in the source/data directory
from datetime import datetime
from source.bot.utils import CogAlert, BaseEmbed, RaiseDBError

class SetBirthday(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setbirthday(self, ctx, *, date: str):
        try:
            datetime.strptime(date, '%d-%m')

            user_id = str(ctx.author.id)
            result = supabase.table("birthdays").insert({"user_id": user_id, "birthday": date}).execute()
            if result:
                await BaseEmbed(ctx, 'Birthday set!', f'Birthday set to {date}!')
                CogAlert(ctx.author.name)
        except Exception as e:
            await RaiseDBError(ctx, e)
            
async def setup(client):
    await client.add_cog(SetBirthday(client))