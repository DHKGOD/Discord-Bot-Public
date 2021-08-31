import datetime
from googletrans import Translator
import discord
from discord.ext import commands
import googletrans
from core.classes import ExtensionBase
import json
from discord.utils import get


class Trans(ExtensionBase):

    @commands.command(aliases=['翻譯', 'tr', '翻', '譯','Trans',])
    async def translate(self, ctx, lang_to, *args):
        reactid = []
        if lang_to == "help":
            with open('trans.json') as f:
                data = json.load(f)
            msg = "hi"

            snipeEmbed = discord.Embed(title=" 翻譯指令使用方法\n > [*tr 語言 訊息]", color=0xDAA520)
            snipeEmbed.add_field(name="** **", value="** **", inline=False)
            snipeEmbed.add_field(name='別名', value="> ***tr , *翻譯 , *翻 , *譯 **", inline=False)
            snipeEmbed.add_field(name="** **", value="** **", inline=False)
            snipeEmbed.add_field(name='反應', value="> ** 按🧐獲取語言表 **", inline=True)
            snipeEmbed.set_footer(text="hi")
            reactions = ["🧐"]

            m = await ctx.send(embed=snipeEmbed)
            for name in reactions:
                emoji = get(ctx.guild.emojis, name=name)
                await m.add_reaction(emoji or name)

        lang_to = lang_to.lower()
        if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES:
            raise commands.BadArgument("BADDDDDDDDDDDDDD")
        text = ''.join(args)
        translator = googletrans.Translator()
        text_translatored = translator.translate(text, dest=lang_to).text
        transembed = discord.Embed(title="> " + text_translatored, color=0xDAA520)
        transembed.set_author(name='中央總書記梅川',
                              icon_url='https://cdn.discordapp.com/avatars/601720742949683201'
                                       '/12f53eaa05b510b0ee524904bd308f68.webp?size=1024')
        transembed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=transembed)


def setup(bot):
    bot.add_cog(Trans(bot))
