import datetime
import datetime, time

import aiohttp
import discord
from discord.ext import commands
from googleapiclient.discovery import build
from core.classes import ExtensionBase
import random
api_key = 'AIzaSyDdsoc2nbE9YZ53vXvSelTZtGKGo304NfI'

class Search(ExtensionBase):

    @commands.command(aliases=["show"])
    async def search(self,ctx, *, search):
        ran = random.randint(0, 9)
        resource = build("customsearch", "v1", developerKey=api_key).cse()
        result = resource.list(
            q=f"{search}", cx="35968fbed304a2d69", searchType="image"
        ).execute()
        url = result["items"][ran]["link"]
        embed1 = discord.Embed(title=f"成功搜尋 : ({search})",color=0xDAA520)
        embed1.set_image(url=url)
        await ctx.send(embed=embed1)

    @commands.command(name='dog')
    async def random_dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://random.中國/woof.json") as r:
                data = await r.json()
                embed = discord.Embed(
                    title="Doggo",
                    color=ctx.author.color
                )
                embed.set_image(url=data['url'])
                await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Search(bot))
