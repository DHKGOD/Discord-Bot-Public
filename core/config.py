import asyncio
import os
import traceback

import discord
from discord.ext import commands
from core.classes import ExtensionBase


class Config(ExtensionBase):

    @commands.command()
    async def unload(self, ctx, cog=None):
        if str(ctx.author.id) != "601720742949683201":
            await ctx.send("你長得不像偉大的梅川中央總書記")
        if str(ctx.author.id) == "601720742949683201":
            if not cog:
                # No cog, means we reload all cogs

                embed = discord.Embed(
                    title="成功移除所有指令",
                    color=0xDAA520,
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir("./cmds/"):
                    if ext.endswith(".py") and not ext.startswith("_"):
                        try:
                            self.bot.unload_extension(f"cmds.{ext[:-3]}")
                            embed.add_field(
                                name=f"成功移除指令: `{ext}`",
                                value='\uFEFF',
                                inline=False
                            )
                        except Exception as e:
                            embed.add_field(
                                name=f"無法移除指令: `{ext}`",
                                value=e,
                                inline=False
                            )

                await ctx.send(embed=embed)
            else:
                # reload the specific cog

                embed = discord.Embed(
                    title="移除中所有指令",
                    color=0xDAA520,
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog.lower()}.py"
                if not os.path.exists(f"./cmds/{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"移除指令失敗: `{ext}`",
                        value="沒有找到這個指令",
                        inline=False
                    )

                elif ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        self.bot.unload_extension(f"cmds.{ext[:-3]}")
                        embed.add_field(
                            name=f"成功移除指令: `{ext}`",
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception:
                        desired_trace = traceback.format_exc()
                        embed.add_field(
                            name=f"移除指令失敗: `{ext}`",

                            inline=False
                        )
                await ctx.send(embed=embed)

    @commands.command()
    async def load(self, ctx, cog=None):
        if str(ctx.author.id) != "601720742949683201":
            await ctx.send("你長得不像偉大的梅川中央總書記")
        if str(ctx.author.id) == "601720742949683201":
            if not cog:
                # No cog, means we reload all cogs

                embed = discord.Embed(
                    title="運行結果",
                    color=0xDAA520,
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir("./cmds/"):
                    if ext.endswith(".py") and not ext.startswith("_"):
                        try:
                            self.bot.load_extension(f"cmds.{ext[:-3]}")
                            embed.add_field(
                                name=f"成功加載指令 : `{ext}`",
                                value='\uFEFF',
                                inline=False
                            )
                        except Exception as e:
                            embed.add_field(
                                name=f"加載指令失敗 : `{ext}`",
                                value=e,
                                inline=False
                            )

                await ctx.send(embed=embed)
            else:
                # reload the specific cog

                embed = discord.Embed(
                    title="運行結果",
                    color=0xDAA520,
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog.lower()}.py"
                if not os.path.exists(f"./cmds/{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"加載指令失敗 : `{ext}`",
                        value="找不到這個指令",
                        inline=False
                    )

                elif ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        self.bot.load_extension(f"cmds.{ext[:-3]}")
                        embed.add_field(
                            name=f"成功加載指令 : `{ext}`",
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception:
                        desired_trace = traceback.format_exc()
                        embed.add_field(
                            name=f"加載指令失敗 : `{ext}`",

                            inline=False
                        )
                await ctx.send(embed=embed)

    @commands.command()
    async def reload(self, ctx, cog=None):
        if str(ctx.author.id) != "601720742949683201":
            await ctx.send("你長得不像偉大的梅川中央總書記")
        if str(ctx.author.id) == "601720742949683201":
            if not cog:
                # No cog, means we reload all cogs

                embed = discord.Embed(
                    title="運行結果",
                    color=0xDAA520,
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir("./cmds/"):
                    if ext.endswith(".py") and not ext.startswith("_"):
                        try:
                            self.bot.unload_extension(f"cmds.{ext[:-3]}")
                            self.bot.load_extension(f"cmds.{ext[:-3]}")
                            embed.add_field(
                                name=f"成功重載指令 : `{ext}`",
                                value='\uFEFF',
                                inline=False
                            )
                        except Exception as e:
                            embed.add_field(
                                name=f"F指令失敗 : `{ext}`",
                                value=e,
                                inline=False
                            )

                await ctx.send(embed=embed)
            else:
                # reload the specific cog

                embed = discord.Embed(
                    title="運行結果",
                    color=0xDAA520,
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog.lower()}.py"
                if not os.path.exists(f"./cmds/{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"指令失敗 : `{ext}`",
                        value="找不到這個指令",
                        inline=False
                    )

                elif ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        self.bot.unload_extension(f"cmds.{ext[:-3]}")
                        self.bot.load_extension(f"cmds.{ext[:-3]}")
                        embed.add_field(
                            name=f"成功重載指令: `{ext}`",
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception:
                        desired_trace = traceback.format_exc()
                        embed.add_field(
                            name=f"指令失敗 : `{ext}`",
                            value=desired_trace,
                            inline=False
                        )
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Config(bot))
