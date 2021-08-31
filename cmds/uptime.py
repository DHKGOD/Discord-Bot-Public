import datetime
import datetime, time
import discord
from discord.ext import commands

from core.classes import ExtensionBase


class Uptime(ExtensionBase):
    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()

    @commands.command(aliases=['ut', 'Uptime'])
    async def uptime(self, ctx, ):
        uptimee = str(datetime.timedelta(seconds=int(round(time.time() - startTime))))
        uptimeembed = discord.Embed(title="UpTime", description="> ** " + uptimee + " **", color=0xDAA520)
        uptimeembed.set_author(name='中央總書記梅川',
                               icon_url='https://cdn.discordapp.com/avatars/601720742949683201'
                                        '/12f53eaa05b510b0ee524904bd308f68.webp?size=1024')

        await ctx.send(embed=uptimeembed)


def setup(bot):
    bot.add_cog(Uptime(bot))
