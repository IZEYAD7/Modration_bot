import discord
from discord.ext import commands
from discord.ext.commands import BucketType
from discord import Member, Embed
from discord import Role
import datetime
class modration(commands.Cog):
    def __init__(self, client):
        self.client = client
    # ban command
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(10, 86400, BucketType.user) # you can change the cooldown of command or delete it  
    @commands.has_guild_permissions(ban_members=True) # you can change the require role for your member 
    @commands.bot_has_guild_permissions(ban_members=True)
    async def ban(self,ctx, member : Member,*,reason=None):
        try:
            await ctx.message.delete()
            async with ctx.typing():
                if ctx.author.top_role > member.top_role :
                    if ctx.guild.me.top_role> member.top_role:
                        if member != ctx.message.guild.owner:
                            if member != ctx.message.guild.me:
                                await member.ban(reason=reason)
                                ban_embed = Embed(title= "BANNED",description= f"**{member.mention}** HAS BEEN BANNED",colour=0x00FFF5, timestamp=datetime.datetime.utcnow())
                                ban_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                                ban_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                                ban_embed.set_thumbnail(url=ctx.guild.icon_url)  
                                await ctx.channel.send(embed=ban_embed, delete_after=10)   
                            else:
                                error3_embed=Embed(title="ERROR", description="YOU DONT HAVE PERMISSION TO BAN **ME**", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                                await ctx.channel.send(embed=error3_embed, delete_after=10)        
                        else:
                            error3_embed=Embed(title="ERROR", description="YOU DONT HAVE PERMISSION TO BAN **SERVER OWNER**", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                            error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                            error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                            error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                            await ctx.channel.send(embed=error3_embed, delete_after=10)
                    else:
                        error3_embed=Embed(title="ERROR", description="I DONT HAVE PERMISSION(**HIGHER ROLE**)", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                        error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                        error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                        error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                        await ctx.channel.send(embed=error3_embed, delete_after=10)
                else:
                    error3_embed=Embed(title="ERROR", description="YOU DONT HAVE PERMISSION(**HIGHER ROLE**)", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                    error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                    error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    await ctx.channel.send(embed=error3_embed, delete_after=10)                           
        except Exception :
            pass
    # kick command    
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(10, 86400, BucketType.user) # you can change the cooldown of command or delete it 
    @commands.has_guild_permissions(kick_members=True) # you can change the require role for your member 
    @commands.bot_has_guild_permissions(kick_members=True) 
    async def kick(self, ctx, member: Member , *, reason = None):
        try:
            await ctx.message.delete()
            async with ctx.typing():
                if ctx.author.top_role > member.top_role :
                    if ctx.guild.me.top_role> member.top_role:
                            if member != ctx.message.guild.owner:
                                if member != ctx.message.guild.me:
                                    await member.kick(reason=reason)
                                    kick_embed = Embed(title= "KICKED",description= f"**{member.mention}** HAS BEEN KICKED",colour=0x00FFF5, timestamp=datetime.datetime.utcnow())
                                    kick_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                                    kick_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                                    kick_embed.set_thumbnail(url=ctx.guild.icon_url)  
                                    await ctx.channel.send(embed=kick_embed, delete_after=10)                                     
                                else:
                                    error3_embed=Embed(title="ERROR", description="YOU DONT HAVE PERMISSION TO KICK **ME**", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                                    error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                                    error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                                    error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                                    await ctx.channel.send(embed=error3_embed, delete_after=10)        
                            else:
                                error3_embed=Embed(title="ERROR", description="YOU DONT HAVE PERMISSION TO KICK **SERVER OWNER**", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                                await ctx.channel.send(embed=error3_embed, delete_after=10)         
                    else:
                        error3_embed=Embed(title="ERROR", description="I DONT HAVE PERMISSION(**HIGHER ROLE**)", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                        error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                        error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                        error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                        await ctx.channel.send(embed=error3_embed, delete_after=10)          
                else:
                    error3_embed=Embed(title="ERROR", description="YOU DONT HAVE PERMISSION(**HIGHER ROLE**)", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                    error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                    error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    await ctx.channel.send(embed=error3_embed, delete_after=10)   
        except Exception :
            pass   
    # change nikcname command 
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(10, 3600, BucketType.user) # you can change the cooldown of command or delete it 
    @commands.has_permissions(manage_nicknames=True)  # you can change the require role for your member 
    @commands.bot_has_guild_permissions(manage_nicknames=True)
    async def nick(self, ctx, member : Member, *,nick):
        try:
            await ctx.message.delete()
            async with ctx.typing():
                if ctx.author.top_role > member.top_role :
                    if ctx.guild.me.top_role> member.top_role:
                        if member != ctx.message.guild.owner:  
                            await member.edit(nick=nick)
                            NICKreject_embed = Embed(title= ("NICKNAME CHANGED"),description= (f"**{member.mention}** NICKNAME HAS BEEN CHANGED TO **{nick}**!"),colour=0x00FFF5, timestamp=datetime.datetime.utcnow())        
                            NICKreject_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                            NICKreject_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                            NICKreject_embed.set_thumbnail(url=ctx.guild.icon_url)  
                            await ctx.channel.send(embed=NICKreject_embed, delete_after=10)     
                        else:
                            error3_embed=Embed(title="ERROR", description="YOU DONT HAVE PERMISSION TO CHANGE NICKNAME OF SERVER OWNER", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                            error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                            error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                            error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                            await ctx.channel.send(embed=error3_embed, delete_after=10)     
                    else:
                        error3_embed=Embed(title="ERROR", description="I DONT HAVE PERMISSION(**HIGHER ROLE**)", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                        error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                        error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                        error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                        await ctx.channel.send(embed=error3_embed, delete_after=10)                
                else:
                    error3_embed=Embed(title="ERROR", description="YOU DONT HAVE PERMISSION(**HIGHER ROLE**)", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                    error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                    error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    await ctx.channel.send(embed=error3_embed, delete_after=10)
        except Exception:
            pass
    # unban command
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True) # you can change the cooldown of command or delete it 
    @commands.bot_has_guild_permissions(ban_members=True)   # you can change the require role for your member
    async def unban(self, ctx, *, member):
        try:
            await ctx.message.delete()
            async with ctx.typing():
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split('#')
                for ban_entry in banned_users:
                    user = ban_entry.user
                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user)
                        mass_embed = Embed(title= ("UNBANNED"),description= (f"{user.name}#{user.discriminator} HAVE BEEN UNBANNED"),colour=0x00FFF5, timestamp=datetime.datetime.utcnow())        
                        mass_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                        mass_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                        mass_embed.set_thumbnail(url=ctx.guild.icon_url)   
                        await ctx.channel.send(embed=mass_embed, delete_after=10) 
        except Exception:
            pass
    # clear command 
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(10, 600, BucketType.channel) # you can change the cooldown of command or delete it 
    @commands.has_permissions(manage_messages=True) # you can change the require role for your member
    @commands.bot_has_guild_permissions(manage_messages=True)
    async def clear(self, ctx, count:int):
        try:
            await ctx.message.delete()
            channel = ctx.channel
            try:
                count = int(count)
            except:
                error3_embed=Embed(title="ERROR", description="PLS GIVE ME A **NUMBER**", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10) 
            async with ctx.typing():
                if count <= 1000:
                    if count > 1:
                        if ctx.channel == channel:
                            await channel.purge(limit=count)
                            your_embed = Embed(title= "DELETED",description= f'**{count}** MESSAGES DELETED' ,colour=0x00FFF5, timestamp=datetime.datetime.utcnow())
                            your_embed.set_thumbnail(url='https://lh3.googleusercontent.com/G2jzG8a6-GAA4yhxx3XMJfPXsm6_pluyeEWKr9I5swUGF62d2xo_Qg3Kdnu00HAmDQ')
                            your_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                            your_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                            await ctx.channel.send(embed=your_embed, delete_after=10)       
                    else:
                        error3_embed=Embed(title="ERROR", description="PLS GIVE ME A NUMBER UPPER THAN **1**", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                        error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                        error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                        error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                        await ctx.channel.send(embed=error3_embed, delete_after=10)                                  
                else:
                    error3_embed=Embed(title="ERROR", description="PLS GIVE ME A NUMBER UNDER **1000**", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                    error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                    error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    await ctx.channel.send(embed=error3_embed, delete_after=10)
        except Exception :
            pass
    # change channel slowmode command
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(10, 3600, BucketType.channel)
    @commands.has_permissions(manage_channels=True) # you can change the cooldown of command or delete it 
    @commands.bot_has_guild_permissions(manage_channels=True) # you can change the require role for your member
    async def slowmode(self, ctx, seconds: int ):
        try:
            await ctx.message.delete()
            channel =  ctx.channel
            try:
                seconds = int(seconds)
            except:
                error3_embed=Embed(title="ERROR", description="PLS GIVE ME A **NUMBER**", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.channel.send(embed=error3_embed, delete_after=10)
            async with ctx.typing():
                secondss =[5, 10, 0, 21600, 7200, 3600, 1800, 900, 600, 300, 120, 60, 30, 15]
                if seconds in secondss:
                    await channel.edit(slowmode_delay=seconds)
                    slow_embed = Embed(title= "SLOWMODE CHANGED!",description= F"SLOWMODE IS **{seconds}** SECONDS NOW IN CHANNEL : **{channel.mention}**!",colour=0x00FFF5, timestamp=datetime.datetime.utcnow())  
                    slow_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    slow_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    slow_embed.set_thumbnail(url=ctx.guild.icon_url)    
                    await ctx.channel.send(embed=slow_embed, delete_after=10)
                else:
                    error3_embed=Embed(title="ERROR", description="PLS GIVE ME A TRUE NUMBER", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                    error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                    error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    await ctx.channel.send(embed=error3_embed, delete_after=10)
        except Exception:
            pass
    # add/remove role command 
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, BucketType.user) # you can change the cooldown of command or delete it 
    @commands.has_guild_permissions(manage_roles=True) # you can change the require role for your member
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def role(self, ctx, role: Role , user : Member):
        try:
            await ctx.message.delete()
            async with ctx.typing():
                if ctx.guild.me.top_role > role :
                    if user.top_role < ctx.author.top_role:
                        if ctx.author.top_role > role:
                            if not role in user.roles: 
                                await user.add_roles(role)
                                role_embed = Embed(title= "ADDED",description= (f'SUCCESFULY ROLE **{role.mention}** ADDED TO **{user.mention}**'),colour=0x00FFF5, timestamp=datetime.datetime.utcnow())
                                role_embed.set_thumbnail(url = self.client.user.avatar_url)
                                role_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                                role_embed.set_author(name=user.name, icon_url=user.avatar_url)
                                await ctx.channel.send(embed=role_embed, delete_after=10)
                            else:                 
                                await user.remove_roles(role)
                                Erole_embed = Embed(title= "REMOVED",description= (f'SUCCESFULY ROLE **{role.mention}** REMOVED FROM **{user.mention}**'),colour=0x00FFF5, timestamp=datetime.datetime.utcnow())
                                Erole_embed.set_thumbnail(url = self.client.user.avatar_url)
                                Erole_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                                Erole_embed.set_author(name=user.name, icon_url=user.avatar_url)
                                await ctx.send(embed=Erole_embed, delete_after=10)     
                        else :
                            error3_embed=Embed(title="ERROR", description="YOU DONT HAVE PERMISSION(HIGHER ROLE)", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                            error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                            error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                            error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                            await ctx.channel.send(embed=error3_embed, delete_after=10)                                
                    else :
                        error3_embed=Embed(title="ERROR", description="YOU DONT HAVE PERMISSION(HIGHER ROLE)", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                        error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                        error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                        error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                        await ctx.channel.send(embed=error3_embed, delete_after=10)                                                 
                else :
                    error3_embed=Embed(title="ERROR", description="YOU DONT HAVE PERMISSION(HIGHER ROLE)", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                    error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                    error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    await ctx.channel.send(embed=error3_embed, delete_after=10)
        except Exception:
            pass
    #lock command
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(5, 3600, BucketType.channel) # you can change the cooldown of command or delete it 
    @commands.has_permissions(manage_permissions=True) # you can change the require role for your member
    @commands.bot_has_guild_permissions(manage_permissions=True)
    async def lock(self, ctx):
        try:
            await ctx.message.delete()
            channel = ctx.channel
            async with ctx.typing():
                overwrite = channel.overwrites_for(ctx.guild.default_role)
                if overwrite.send_messages != False:
                    overwrite.send_messages = False
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                    unlock_embed = Embed(title= ("LOCKED"),description= (f"**{channel.mention}** HAS BEEN LOCKED FOR **{ctx.guild.default_role}**"),colour=0x00FFF5, timestamp=datetime.datetime.utcnow())        
                    unlock_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    unlock_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    unlock_embed.set_thumbnail(url=ctx.guild.icon_url)    
                    await ctx.channel.send(embed=unlock_embed, delete_after=10)
                else :
                    error3_embed=Embed(title="ERROR", description="CHANNEL HAS ALREADY BEEN **LOCKED**", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                    error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                    error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    await ctx.channel.send(embed=error3_embed, delete_after=10)
        except Exception :
            pass
    #unlock command
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(5, 3600, BucketType.channel)
    @commands.has_permissions(manage_permissions=True) # you can change the cooldown of command or delete it
    @commands.bot_has_guild_permissions(manage_permissions=True) # you can change the require role for your member
    async def unlock(self, ctx):
        try:
            await ctx.message.delete()
            channel = ctx.channel
            async with ctx.typing():
                overwrite = channel.overwrites_for(ctx.guild.default_role)
                if overwrite.send_messages != True:
                    overwrite.send_messages = True
                    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                    unlock_embed = Embed(title= ("UNLOCKED"),description= (f"**{channel.mention}** HAS BEEN UNLOCKED FOR **{ctx.guild.default_role}**"),colour=0x00FFF5, timestamp=datetime.datetime.utcnow())        
                    unlock_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    unlock_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    unlock_embed.set_thumbnail(url=ctx.guild.icon_url)    
                    await ctx.channel.send(embed=unlock_embed, delete_after=10)
                else :
                    error3_embed=Embed(title="ERROR", description="CHANNEL HAS ALREADY BEEN **UNLOCKED**", colour=0xff0000, timestamp=datetime.datetime.utcnow())
                    error3_embed.set_thumbnail(url='https://images.emojiterra.com/google/android-11/512px/274c.png')
                    error3_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
                    error3_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    await ctx.channel.send(embed=error3_embed, delete_after=10)
        except Exception :
            pass
def setup(client):
    client.add_cog(modration(client))
    
        

                                                                           