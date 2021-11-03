import discord
from discord.ext import commands
from discord import Embed, Member
from discord.ext.commands import BucketType
from typing import Optional
import datetime
class misc(commands.Cog):
    def __init__(self, client):
        self.client = client
    #avatar command
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, BucketType.user) # you can change the cooldown of command or delete it 
    async def avatar(self, ctx, target:Optional[Member]):
        target = target or ctx.author
        avatar_embed = Embed(title= ("AVATAR"),description= (f"{target.mention}"),colour=0x00FFF5, timestamp=datetime.datetime.utcnow())           
        avatar_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        avatar_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        avatar_embed.set_thumbnail(url = ctx.guild.icon_url)
        avatar_embed.set_image( url = target.avatar_url)
        await ctx.channel.send(embed=avatar_embed)
    #user information command
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, BucketType.user) # you can change the cooldown of command or delete it 
    async def user(self, ctx, target:Optional[Member]):
        await ctx.message.delete()
        target = target or ctx.author
        userinfo_embed = Embed(title= ("USER INFORMATION"),colour=0x00FFF5, timestamp=datetime.datetime.utcnow())
        fields = [("ID", target.id, False),
                ("NAME", str(target), False),
                ("BOT?", target.bot, False),
                ("TOP ROLE", target.top_role.mention, False),
                ("CREATED AT", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                ("JOINED AT", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                ("BOOSTED", bool(target.premium_since), False)] 
        for name, value, inline in fields:
            userinfo_embed.add_field(name=name, value=value, inline=inline)
        userinfo_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        userinfo_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        userinfo_embed.set_thumbnail(url = ctx.guild.icon_url)
        userinfo_embed.set_image( url = target.avatar_url)
        await ctx.channel.send(embed=userinfo_embed)
    #server information command            
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, BucketType.user) # you can change the cooldown of command or delete it 
    async def server(self, ctx):
        await ctx.message.delete()
        server_embed = Embed(title= ("SERVER INFORMATION"),colour=0x00FFF5, timestamp=datetime.datetime.utcnow())
        statuses=[len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members))),]    
        fields =[("STATUSES", f"🟢 {statuses[0]} 🟡 {statuses[1]} 🔴 {statuses[2]} 🔘 {statuses[3]}", False), 
                ("ID", ctx.guild.id, True),
                ("Owner:", ctx.guild.owner.mention, True),
                ("REGION", ctx.guild.region, True),
                ("CREATED AT", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                ("MEMBERS", len(ctx.guild.members), True),
                ("HUMANS", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                ("BOTS", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                ("TEXT CHANNELS", len(ctx.guild.text_channels), True),
                ("VOICE CHANNELS", len(ctx.guild.voice_channels), True),
                ("CATEGORIES", len(ctx.guild.categories),True),
                ("BANNED MEMBERS", len(await ctx.guild.bans()), True),
                ("ROLES", len(ctx.guild.roles), True),] 
        for name, value, inline in fields:
            server_embed.add_field(name=name, value=value, inline=inline)     
        server_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        server_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        server_embed.set_image(url =ctx.guild.icon_url)
        await ctx.channel.send(embed=server_embed)    
    # server avatar command        
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10, BucketType.user) # you can change the cooldown of command or delete it 
    async def server_avatar(self, ctx):
        await ctx.message.delete() 
        avatar_embed = Embed(title= ("AVATAR"),description= (f"{ctx.guild.name}"),colour=0x00FFF5, timestamp=datetime.datetime.utcnow())           
        avatar_embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        avatar_embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        avatar_embed.set_image(url=ctx.guild.icon_url)
        await ctx.channel.send(embed=avatar_embed)   
def setup(client):
    client.add_cog(misc(client))        