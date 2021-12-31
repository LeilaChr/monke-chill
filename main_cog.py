import discord
from replit import db
from discord.ext import commands
from random import choice
import requests
import asyncio 
import json
class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
General commands:
?help - Displays all the available commands
?credits - This command returns the TRUE credits
?hello - This command returns a random welcome message
?die - This command returns a random last words
?quote - This command returns a random quote
?ping - This command returns the latency

Music commands:
?play <keywords> - Finds the song on youtube and plays it in your current channel
?queue - Displays the current music queue
?skip - Skips the current song being played
?pause - This command pauses the song
?resume - Resumes the song
?leave - Disconnecting bot from VC
?remove <number> - Removes a song from the queue with index starting at 0
```
"""
        self.hello = """
```
No one but me, lozer!
```
"""
        self.sad_words = ["sad","kms", "depressed", "unhappy", "angry", "miserable", "depressing"]

        self.options = [
        "Don't listen to Stews. He lies. Cheer up!",
        "Don't listen to Stews. He lies. Hang in there.",
        "Don't listen to Stews. He lies. You are a great person / bot!"
        ]
        

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)


    @commands.command(name='credits', help='This command returns the TRUE credits')
    async def creditz(self,ctx):
        await ctx.send(self.hello)
    
    @commands.command(name='hello', help='This command returns a random welcome message')
    async def hello(self,ctx):
        responses = ['***Grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
        await ctx.send(choice(responses))

    @commands.command(name='die', help='This command returns a random last words')
    async def die(self,ctx):
        responses = ['Why have you brought my short life to an end', 'I could have done so much more', 'I have a family, kill them instead']
        await ctx.send(choice(responses))
    
    @commands.command(name='ping', help='This command returns the latency')
    async def ping(self,ctx: commands.Context):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command(name='quote', help='This command returns the latency')
    async def quote(self,ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        await ctx.send(quote)

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        if any(word in msg for word in self.sad_words):
            await asyncio.sleep(1)
            await message.channel.send(choice(self.options)) 