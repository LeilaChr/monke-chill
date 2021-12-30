import discord
import os
import requests
import json
import random
from replit import db
from discord.ext import commands
import youtube_dl
from keep_alive import keep_alive
from main_cog import main_cog
from music_cog import music_cog



#import all of the cogs


bot = commands.Bot(command_prefix='?')


#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(main_cog(bot))
bot.add_cog(music_cog(bot))




keep_alive()
#start the bot with our token
bot.run(os.getenv("TOKEN"))