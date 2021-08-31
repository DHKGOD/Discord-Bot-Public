import datetime

import discord
import youtube_dl
from discord.ext import commands
from youtube_dl.postprocessor import ffmpeg

import music
from core.classes import ExtensionBase
from discord.utils import get


class Speaker(ExtensionBase):

    @commands.command()
    async def join(self, ctx):
        botvoice = get(ctx.bot.voice_clients, guild=ctx.guild)
        print(botvoice)

        if ctx.author.voice is None:
            await ctx.send("你不在語音頻道")
        if ctx.author.voice is not None and botvoice is None:
            await ctx.author.voice.channel.connect()
        else:
            await ctx.guild.voice_client.move_to(ctx.author.voice.channel)

    @commands.command()
    async def leave(self, ctx):
        botvoice = get(ctx.bot.voice_clients, guild=ctx.guild)
        if botvoice is None:
            await ctx.send("我不在語音頻道")
        else:
            await ctx.guild.voice_client.disconnect()



def setup(bot):
    bot.add_cog(Speaker(bot))
