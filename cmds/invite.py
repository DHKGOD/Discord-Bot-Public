import datetime

import discord
from discord.ext import commands

from core.classes import ExtensionBase


class Invite(ExtensionBase):

    @commands.command(aliases=['邀請', 'inv','Invite'])
    async def invite(self, ctx):
        embedVar = discord.Embed(
            description='[:flag_cn:  邀請(Invite)  :flag_cn:]('
                        'https://discord.com/api/oauth2/authorize?client_id=880824023863418950&permissions=8&scope=bot'
                        '=bot "邀請習維尼去你的伺服器")',
            color=0xDAA520)
        embedVar.set_author(name='中央總書記梅川',
                            icon_url='https://cdn.discordapp.com/avatars/601720742949683201'
                                     '/12f53eaa05b510b0ee524904bd308f68.webp?size=1024')
        embedVar.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedVar)


def setup(bot):
    bot.add_cog(Invite(bot))
