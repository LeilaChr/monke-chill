import discord
from discord.ext import commands
from random import choice
from discord import Member
import requests, time, os
import asyncio 
import json
import spacy
from urllib.request import urlopen
from bs4 import BeautifulSoup


class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
**General commands**
?help - Displays all the available commands
?credits - This command returns the TRUE credits
?hello - This command returns a random welcome message
?die - This command returns random last words
?quote - This command returns a random quote
?ping - This command returns the latency
?birthday - This command displays a special birthday message
?darquote - This command returns a dark quote 
?joke [arg]- This command returns a random joke (arg = one if you want a one part joke)
?dadjoke - This command returns a random dad joke
?yomamma - This command returns a random yo mamma joke
?dictionary [arg] - This command returns the urban dictionary definition 
?pfp [arg] - This command returns profile picture of user
?banner [arg]- This command returns the profile banner
?mock - This command returns the mock emoji
?shock - This command returns the shock emoji
?dog - This command returns the dog emoji
?hack - This command returns the hack emoji
```
"""
        self.help_message_music = """
```
Music commands:
?play <keywords> - Finds the song or playlist on youtube and plays it in your current channel.
?queue - Displays the current music queue
?skip - Skips the current song being played
?pause - This command pauses the song
?resume - Resumes the song
?stop - Disconnecting bot from VC
?remove <number> - Removes a song from the queue with index starting at 0
?np - Shows current song
```
"""
        self.hello = """
```
No one but me!
```
"""
        self.sad_words = ["sad","kms", "depressed", "unhappy", "miserable", "depressing","fml","fuck my life","misery"]

        self.age = 19


    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)


    @commands.command(name='credits', help='This command returns the TRUE credits')
    async def creditz(self,ctx):
        await ctx.send(self.hello)
    
    @commands.command(name='hello', help='This command returns a random welcome message')
    async def hello(self,ctx):
          response = requests.get("https://www.greetingsapi.com/random")
          json_data = json.loads(response.text)
          setup = json_data["greeting"]
          await ctx.send("**"+setup + "**" + " This is hello in " + json_data["language"])  

    @commands.command(name='die', help='This command returns a random last words')
    async def die(self,ctx):
        responses = ['Why have you brought my short life to an end', 'I could have done so much more', 'I have a family, kill them instead','It\'s better to burn out than to fade away. -Kurt Cobain','All compounded things are subject to vanish. Strive with earnestness. -Buddha','Relax - This won\'t hurt. -Hunter S. Thompson','I hope I haven\'t bored you. -Elvis Presley','Just don\'t leave me alone. -John Belushi','I do not believe in my death. -Salavdor Dali','Adieu, mes amis. Je vais Ã  la gloire. (Farewell, my friends. I go to glory.) -Isadora Duncan','I believe that a life lived for music is an existence spent wonderfully, and this is what I have dedicated my life to. -Luciano Pavarotti','Tell them I\'ve had a wonderful life. -Ludwig Wittgenstein','Friends applaud, the comedy is over. -Beethoven','I should have never switched from Scotch to martinis. -Humphrey Bogart','Let no one weep for me, or celebrate my funeral with mourning; for I still live, as I pass to and fro through the mouths of men. -Ennius','It matters not how strait the gate, How charged with punishments the scroll, I am the master of my fate: I am the captain of my soul. —Timothy McVeigh','Yes, I would just like to say I\'m sailing with the rock, and I\'ll be back, like Independence Day, with Jesus. June 6, like the movie. Big mother ship and all, I\'ll be back, I\'ll be back. —Aileen Wuornos','Leave me alone, I\'m fine. —Barry White','I\'d like to thank the Academy for my lifetime achievement award that I will eventually get.—Donald O','Jeb. Just remember, whatever happens, happens. —Dwain Weston','Now I\'ll show you how an Italian dies! -Fabrizio Quattrocchi','Let me go to the house of the Father. -Pope John Paul II','Don\'t die like I did. -George Best','My last words will be \"Hoka Hey, it\'s a good day to die.\" Thank you very much. I love you all. Goodbye. — Clarence Ray Allen','C\'mon. Let\'s get this day over and done with. -Peter Brock','And if I should ever die, God forbid, I hope you will say: \'Kurt is up in heaven now\'. That\'s my favorite joke. -Kurt Vonnegut','Katie, Katie, look, it\'ll be fine, you know, I just need to get some sleep. -Heath Ledger','I\'m the happiest man in the world. I\'ve just summited a beautiful mountain. -Clifton Maloney']
        await ctx.send(choice(responses))

    @commands.command(name='darquote', help='This command returns a random dark quote/humor')
    async def darquote(self,ctx):
        responses = ['I need a hug from the line 1', 'Dark humor is like food, not everyone gets it.', 'Boutta put a period at the end of my life sentence',
                     'When will side character get offed?','My spirit animal is a dragon because I aspire to not exist like it','Is there a purpose to having a purpose?',
                     'Am I even worthy of being a burden?','My favorite party trick is becoming the piñata when nobody expects it',
                     'The future is a camera with a covered shutter,ever running but always dark','Almost over the edge might drive over the edge']
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
                print("hello")
        

    @commands.command(name='birthday', help='This command displays a special birthday message')            
    async def birthday(self,ctx,*args):
        msg=''
        if len(args)==0 or args[0]=='<@!143449835771527169>':
          msg = 'Happy Birthday!!!\n<a:neonpartyblob:929500659055722526> <a:partyCatJam:929500684322238494>'+  '<@143449835771527169>'+'<a:partyCatJam:929500684322238494><a:neonpartyblob:929500659055722526>\n You are '+ str(self.age) + ' years old'
          self.age+=1
        else:  
          msg= 'Happy Birthday!!!\n<a:neonpartyblob:929500659055722526> <a:partyCatJam:929500684322238494>'+ args[0]+'<a:partyCatJam:929500684322238494><a:neonpartyblob:929500659055722526>' 
        await ctx.send(msg)  
     
    @commands.command(name='dictionary', help='This command returns dictionary') 
    async def dictionary(self,ctx,*args):
        if len(args)==0:
            await ctx.send('https://www.merriam-webster.com/')
        elif len(args) == 1:
            await ctx.send("https://www.urbandictionary.com/define.php?term="+args[0])
        else:
            arg=args[0]
            for i in range(1,len(args)):
                arg+="%20"
                arg+=args[i]
            await ctx.send("https://www.urbandictionary.com/define.php?term="+arg)

            
    @commands.command(name='shock')
    async def shock(self,ctx):
            await ctx.send('<a:pika:991390588920401964>')

            
    @commands.command(name='hack')
    async def hack(self,ctx):
            await ctx.send('<a:Heccer:991398539181690910>')

        
    @commands.command(name='pfp')
    async def pfp(self,ctx,*args):
            if (ctx.message.mentions.__len__()>0):
                for user in ctx.message.mentions:
                    await ctx.send(user.avatar_url)
            else:
                await ctx.send(ctx.message.author.avatar_url)

    @commands.command(name='mock')
    async def mock(self,ctx):
        await ctx.send('<:mock:992259532610883675>')


    @commands.command(name='dog')
    async def dog(self,ctx):
        await ctx.send('<:dog:992262018658742372>')



    @commands.command(name='server')
    async def servers(self, ctx):
        activeservers = self.bot.guilds
        for guild in activeservers:
            await ctx.send(guild.name)
            print(guild.name)

    @commands.command()
    async def banner(self,ctx,*args):
        if (ctx.message.mentions.__len__()>0):
            for user in ctx.message.mentions:
                req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
                banner_id = req["banner"]
                # If statement because the user may not have a banner
                if banner_id:
                    banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
                    await ctx.send(f"{banner_url}")
                else:
                    await ctx.send(user.name + " has no banner!")
        else:            
            user = ctx.author
            req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
            banner_id = req["banner"]
            # If statement because the user may not have a banner
            if banner_id:
                banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
                await ctx.send(f"{banner_url}")
            else:
                await ctx.send("You don't have a banner!")

    @commands.command()
    async def joke(self,ctx,*args):
        if( len(args) !=0 and args[0] == "one"):
          response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
          json_data = json.loads(response.text)
          setup = json_data["joke"]
          await ctx.send(setup)  
        else:   
          response = requests.get("https://v2.jokeapi.dev/joke/Any?type=twopart")
          json_data = json.loads(response.text)
          setup = json_data["setup"]
          punchline = json_data["delivery"]
          await ctx.send(setup+"\n" + "||" + punchline +"||")
        
    @commands.command()
    async def dadjoke(self,ctx):
         nlp = spacy.load('en_core_web_sm')
         joke = requests.get('https://icanhazdadjoke.com/',
                             headers={"Accept": "text/plain"}).text
         output=""
         for index, sentence in enumerate(nlp(joke).sents):
             if index == 0:
                 s = f"{sentence}\n"
             elif index == 1:
                 s = f"||{sentence}||"
             else:
                 s = sentence
             output = f"{output} {s}"
         await ctx.send(output)     


    @commands.command()
    async def yomamma(self,ctx,*args):
          response = requests.get("https://api.yomomma.info/")
          json_data = json.loads(response.text)
          setup = json_data["joke"]
          await ctx.send(setup)      
