import discord
from discord import Embed
from discord.ext import commands
import datetime
class anti_link(commands.Cog):
    def __init__(self, client):
        self.client=client
    @commands.Cog.listener()
    async def on_message(self, message): 
    #links//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////                   
        if "https://" in message.content.lower():
            if message.channel.id != 873155455478804500 :
                await message.delete()
                mo_embed = Embed(title= "DELETED", description= ' MESSAGE DELETED' , colour=0xff0000, timestamp=datetime.datetime.utcnow())
                mo_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                mo_embed.set_thumbnail(url='https://cdn-0.emojis.wiki/emoji-pics/messenger/cross-mark-messenger.png')
                await message.channel.send(embed=mo_embed, delete_after=10)             
        if "discord.gg" in message.content.lower():
            if message.channel.id != 873155455478804500 :
                await message.delete()
                mo_embed = Embed(title= "DELETED", description= ' MESSAGE DELETED' , colour=0xff0000, timestamp=datetime.datetime.utcnow())
                mo_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                mo_embed.set_thumbnail(url='https://cdn-0.emojis.wiki/emoji-pics/messenger/cross-mark-messenger.png')
                await message.channel.send(embed=mo_embed, delete_after=10) 
        if "https" in message.content.lower():
            await message.delete()
            mo_embed = Embed(title= "DELETED", description= ' MESSAGE DELETED' , colour=0xff0000, timestamp=datetime.datetime.utcnow())
            mo_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            mo_embed.set_thumbnail(url='https://cdn-0.emojis.wiki/emoji-pics/messenger/cross-mark-messenger.png')
            await message.channel.send(embed=mo_embed, delete_after=10)     
        if "www." in message.content.lower():
            if message.channel.id != 873155455478804500 :
                await message.delete()
                mo_embed = Embed(title= "DELETED", description= 'MESSAGE DELETED' , colour=0xff0000, timestamp=datetime.datetime.utcnow())
                mo_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                mo_embed.set_thumbnail(url='https://cdn-0.emojis.wiki/emoji-pics/messenger/cross-mark-messenger.png')
                await message.channel.send(embed=mo_embed, delete_after=10)   
def setup(client):
    client.add_cog(anti_link(client))        