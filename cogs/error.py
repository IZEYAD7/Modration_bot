import discord
from discord.ext import commands
from discord import Member,Embed
class error(commands.Cog):
    def __init__(self,client):
        self.client=client
        self._last_member = None
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        async with ctx.typing():
            if isinstance(error, commands.NoPrivateMessage):
                error3_embed=Embed(title="ERROR", description=f"THIS IS A **DM** {ctx.author.mention} TRY THIS COMMAND ON A **SERVER**!", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)    
            elif isinstance(error, commands.CommandOnCooldown):
                error3_embed=Embed(title="ERROR", description=f"TRY AGAIN IN **{error.retry_after:.2f}**s", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)
            elif isinstance(error, commands.MissingPermissions): 
                error3_embed=Embed(title="ERROR", description="**YOU** DONT HAVE PERMISSION", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)         
            elif isinstance(error, commands.BotMissingPermissions):   
                error3_embed=Embed(title="ERROR", description="**I** DONT HAVE PERMISSION", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)  
            elif isinstance(error, commands.MissingRequiredArgument):  
                error3_embed=Embed(title="ERROR", description="YOU ARE MISSIONG **REQUIRED ARGUMENT** USE **HELP** COMMAND!", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)
            elif isinstance(error, commands.MemberNotFound):
                error3_embed=Embed(title="ERROR", description=f"PLS ENTER A TRUE **MEMBER**", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)   
            elif isinstance(error, commands.ChannelNotFound):
                error3_embed=Embed(title="ERROR", description=f"PLS ENTER A TRUE **CHANNEL**", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10) 
            elif isinstance(error, commands.EmojiNotFound):
                error3_embed=Embed(title="ERROR", description=f"PLS ENTER A TRUE **EMOJI**", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)           
            elif isinstance(error, commands.ChannelNotReadable):
                error3_embed=Embed(title="ERROR", description=f"I DON'T HAVE PERMISSIONS TO **READ THIS CHANNEL**", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)    
            elif isinstance(error, commands.GuildNotFound):
                error3_embed=Embed(title="ERROR", description=f"I CAN'T FIND THIS **GUILD**", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)   
            elif isinstance(error, commands.BadColourArgument):
                error3_embed=Embed(title="ERROR", description=f"I CAN'T FIND THIS **COLOR**", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)                                
            elif isinstance(error, commands.UserNotFound):  
                error3_embed=Embed(title="ERROR", description="ENTER TRUE **USER**", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10) 
            elif isinstance(error, commands.RoleNotFound):  
                error3_embed=Embed(title="ERROR", description="ENTER TRUE **ROLE**", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)     
            elif isinstance(error, commands.MessageNotFound):  
                error3_embed=Embed(title="ERROR", description="ENTER TRUE **MESSAGE**", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)                                 
            elif isinstance(error, commands.BadArgument):  
                error3_embed=Embed(title="ERROR", description="ENTER **TRUE** ARGUMENT", colour=0xff0000)
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)      
def setup(client):
    client.add_cog(error(client)) 