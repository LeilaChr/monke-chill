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
from snipe_cog import snipe_cog


bot = commands.Bot(command_prefix='?')


#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(main_cog(bot))
async def setup():
    await bot.wait_until_ready()
    bot.add_cog(music_cog(bot))

bot.loop.create_task(setup())
#bot.add_cog(music_cog(bot))
bot.add_cog(snipe_cog(bot))



keep_alive()
#start the bot with our token
bot.run(os.getenv("TOKEN"))