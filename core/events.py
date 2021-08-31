import os

import discord
import youtube_dl
from discord.ext import commands
from core.classes import ExtensionBase
import json


class Events(ExtensionBase):
    @commands.Cog.listener()
    async def on_message(self, message):
        mention = f'<@!{self.bot.user.id}>'
        mentions = f'<@!{601720742949683201}>'
        if mention in message.content and "av" not in message.content:
            await message.reply("用 *help 使用 習皇帝BOT")
        if mentions in message.content and "av" not in message.content:
            await message.reply("抓到 偷Tag 哈哈")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        with open('trans.json') as f:
            transjson = json.load(f)
        msg = await self.bot.get_channel(data.channel_id).fetch_message(data.message_id)
        author = msg.author
        dmid = data.member
        if str(data.emoji) == "🧐" and author == self.bot.user:
            transjsonString = str(transjson).replace("{", "[")
            await dmid.send("```語言表: " + transjsonString.replace("}", "]") + "```")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("中共國沒這項指令!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("習皇帝找不到你的參數!")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("指令錯誤，Google吧!")



def setup(bot):
    bot.add_cog(Events(bot))
