import datetime

import discord
from discord.ext import commands

from core.classes import ExtensionBase


class Talk(ExtensionBase):
    @commands.command(pass_context=True,aliases=['Talk'])
    async def talk(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)




def setup(bot):
    bot.add_cog(Talk(bot))
