import datetime

import discord

from discord.ext import commands
import os
import music

prefix = '*'
token = 'ODgwODI0MDIzODYzNDE4OTUw.YSj5TA.6q8w4K3anm_TIGlwcOTOlMdohnk'
maybottoken = 'ODYyMTc3NzE2MjE2NjYwMDM4.YOUjkg.3VWB02kFWX3Y1l8wEIA28vhHxYI'

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
    bot.run('ODgwODI0MDIzODYzNDE4OTUw.YSj5TA.6q8w4K3anm_TIGlwcOTOlMdohnk')
