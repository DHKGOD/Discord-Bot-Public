import datetime
import datetime, time
import discord
import gtts
from discord.ext import commands
from gtts import gTTS
from core.classes import ExtensionBase


class speaker(ExtensionBase):
    @commands.command()
    async def speaker(self, ctx, msg,*h):
     await ctx.send(msg)
     print(h)



def setup(bot):
    bot.add_cog(speaker(bot))
