import datetime

import discord

from discord.ext import commands
import os
import music

prefix = '*'


bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="中國割韭菜大戰"))
    print('Bot is Online ! !')


for coree in os.listdir('./core'):
    if coree.endswith(".py") and "classes" not in coree:
        bot.load_extension(f'core.{coree[:-3]}')


for music in os.listdir('./music'):
    if music.endswith(".py"):
        bot.load_extension(f'music.{music[:-3]}')

for filename in os.listdir('./cmds'):
    if filename.endswith(".py") :
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run()
