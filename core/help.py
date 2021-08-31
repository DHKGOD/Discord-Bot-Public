import datetime
import math

import discord
from discord.ext import commands

from core.classes import ExtensionBase


class Help(ExtensionBase):
    @commands.command(aliases=['Help'])
    async def help(self, ctx):
        Helpembed = discord.Embed(title="幫助(Help)",
                                  description='[\u2605  邀請(Invite)  \u2605]('
                                              'https://discord.com/api/oauth2/authorize?client_id=880824023863418950&permissions=8&scope=bot'
                                              '=bot "邀請習維尼去你的伺服器")',
                                  color=0xDAA520)
        Helpembed.set_author(name='中央總書記梅川',
                             icon_url='https://cdn.discordapp.com/avatars/601720742949683201'
                                      '/12f53eaa05b510b0ee524904bd308f68.webp?size=1024')
        Helpembed.add_field(name='指令(Commands)',
                            value="> ** Avatar **" + "`查看別人的頭貼`\n" + "> ** China **" + "`永遠跟著黨走，閱讀黨的心靈雞湯`\n" + "> ** Invite **" + "`邀請習皇帝到你家割韭菜`\n" + "> ** Sinple **" + "`查看最新已刪除的訊息`\n" + "> **  Talk **" + "`讓機器人說出你想說的(不適用於中國)`\n"+"> ** Trans **"+"`翻譯，讓你學會各國語言`\n" +"> ** Uptime **"+"`查看機器人開機時間`\n"+"> ** Commands **"+"`查看指令如何使用`" ,
                            inline=True)
        Helpembed.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=Helpembed)


def setup(bot):
    bot.add_cog(Help(bot))
