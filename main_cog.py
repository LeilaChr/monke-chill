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
        self.sad_words = ["sad","kms", "depressed", "unhappy", "miserable", "depressing","fml","fuck my life","misery"]

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
        responses = ['Why have you brought my short life to an end', 'I could have done so much more', 'I have a family, kill them instead','It\'s better to burn out than to fade away. -Kurt Cobain','All compounded things are subject to vanish. Strive with earnestness. -Buddha','Relax - This won\'t hurt. -Hunter S. Thompson','I hope I haven\'t bored you. -Elvis Presley','Just don\'t leave me alone. -John Belushi','I do not believe in my death. -Salavdor Dali','Adieu, mes amis. Je vais Ã  la gloire. (Farewell, my friends. I go to glory.) -Isadora Duncan','I believe that a life lived for music is an existence spent wonderfully, and this is what I have dedicated my life to. -Luciano Pavarotti','Tell them I\'ve had a wonderful life. -Ludwig Wittgenstein','Friends applaud, the comedy is over. -Beethoven','I should have never switched from Scotch to martinis. -Humphrey Bogart','Let no one weep for me, or celebrate my funeral with mourning; for I still live, as I pass to and fro through the mouths of men. -Ennius','It matters not how strait the gate, How charged with punishments the scroll, I am the master of my fate: I am the captain of my soul. —Timothy McVeigh','Yes, I would just like to say I\'m sailing with the rock, and I\'ll be back, like Independence Day, with Jesus. June 6, like the movie. Big mother ship and all, I\'ll be back, I\'ll be back. —Aileen Wuornos','Leave me alone, I\'m fine. —Barry White','I\'d like to thank the Academy for my lifetime achievement award that I will eventually get.—Donald O','Jeb. Just remember, whatever happens, happens. —Dwain Weston','Now I\'ll show you how an Italian dies! -Fabrizio Quattrocchi','Let me go to the house of the Father. -Pope John Paul II','Don\'t die like I did. -George Best','My last words will be \"Hoka Hey, it\'s a good day to die.\" Thank you very much. I love you all. Goodbye. — Clarence Ray Allen','C\'mon. Let\'s get this day over and done with. -Peter Brock','And if I should ever die, God forbid, I hope you will say: \'Kurt is up in heaven now\'. That\'s my favorite joke. -Kurt Vonnegut','Katie, Katie, look, it\'ll be fine, you know, I just need to get some sleep. -Heath Ledger','I\'m the happiest man in the world. I\'ve just summited a beautiful mountain. -Clifton Maloney']
        await ctx.send(choice(responses))
    
    @commands.command(name='ping', help='This command returns the latency')
    async def ping(self,ctx: commands.Context):

        await ctx.send(f"Pong <:forced_smile:926234553096491041> ! {round(self.bot.latency * 1000)}ms")

    @commands.command(name='quote', help='This command returns the latency')
    async def quote(self,ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        await ctx.send(quote)

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        for word in self.sad_words:
            if (' ' + word + ' ') in (' ' + msg.lower() + ' ') :
                await asyncio.sleep(1)
                await message.channel.send(choice(self.options))


