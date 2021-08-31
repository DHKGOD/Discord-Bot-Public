from discord.ext import commands
import discord
import json


class ExtensionBase(commands.Cog):
	def __init__(self, bot, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.bot = bot
