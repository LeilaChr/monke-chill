import discord
from discord.ext import commands
from random import choice
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
?quotes - Coming soon
?ping - This command returns the latency

Music commands:
?play <keywords> - Finds the song on youtube and plays it in your current channel
?queue - Displays the current music queue
?skip - Skips the current song being played
?pause - This command pauses the song
?resume - Resumes the song
?leave - Disconnecting bot from VC
```
"""
        self.hello = """
```
No one but me, lozer!
```
"""
    
    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)


    @commands.command(name='credits', help='This command returns the TRUE credits')
    async def creditz(self,ctx):
        await ctx.send(self.hello)
    
    @commands.command(name='hello', help='This command returns a random welcome message')
    async def hello(self,ctx):
        responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
        await ctx.send(choice(responses))

    @commands.command(name='die', help='This command returns a random last words')
    async def die(self,ctx):
        responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
        await ctx.send(choice(responses))
    
    @commands.command(name='ping', help='This command returns the latency')
    async def ping(self,ctx: commands.Context):
        await ctx.send(f"Pong <:forced_smile:926234553096491041>! {round(self.bot.latency * 1000)}ms")