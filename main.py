#Made by GuyTonic/Corey 
import random
from discord import Intents, Message
import datetime
import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import os
import asyncio
from typing import Final
from Responses import get_response,get_gamechangerlist



load_dotenv(find_dotenv()) #This is where the discord Token is hidden yall can't have this
TOKEN: Final = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default() 
intents.message_content = True

#########################################bot function#########################################

bot = commands.Bot(command_prefix="---", intents=intents, case_insensitive=True)

# ID for my personal server
@bot.event # on bot start up
async def on_ready():
    channel = bot.get_channel(1222252767046013079) #bot testing channel
    print(f"Logged in as {bot.user}")
    await channel.send('Hello world ') 

@bot.command() #Shut down command
@commands.is_owner()
async def shutdown(ctx):
    channel = bot.get_channel(1222252767046013079) #bot testing channel
    await channel.send('logging off')
    await bot.close()
        
@bot.command()  # Command for the Game Changer list
async def gamechanger(ctx):
    gamechanger_list = []
    gamechanger_list= get_gamechangerlist()
    await ctx.send(gamechanger_list[0])
    await ctx.send(gamechanger_list[1])
    
        
@bot.command() #for the !quote command
async def Quote(ctx):
    response = get_response()
    await ctx.send(response)
    
@bot.command()
@commands.is_owner()

async def speak(ctx, channel_id: int, *, message: str):
    
    # Fetch the channel by ID
    target_channel = bot.get_channel(channel_id)
    if target_channel is None:
        await ctx.send("Couldn't find that channel.")
        return

    try:
        await target_channel.send(message)
        await ctx.send(f"Message sent to <#{channel_id}>!")
    except Exception as e:
        await ctx.send(f"Failed to send message: {e}")

@bot.command()
@commands.has_permissions(administrator=True) 

async def repeat(ctx, *, args: str):

    # Check if a channel was mentioned
    if ctx.message.channel_mentions:
        target_channel = ctx.message.channel_mentions[0]  # Use the first mentioned channel
        # Remove the channel mention from the message text
        message = args.replace(f"<#{target_channel.id}>", "").strip()
    else:
        target_channel = ctx.channel
        message = args

    await target_channel.send(message)
            
############################# Moderation ################################

@bot.command()
@commands.has_permissions(administrator=True) 

async def timeout(ctx, member: discord.Member, duration: int, *, reason="No reason provided"):
    try:
        duration *= 60
        until = discord.utils.utcnow() + datetime.timedelta(seconds=duration)
        await member.timeout(until, reason=reason)
        await ctx.send(f"{member.mention} has been timed out for {duration} seconds. Reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I don't have permission to timeout this user.")
            
@bot.command()
@commands.has_permissions(moderate_members=True)
async def untimeout(ctx, member: discord.Member, *, reason="No reason provided"):
    try:
        await member.timeout(None, reason=reason)
    except discord.Forbidden:
        await ctx.send("I don't have permission to untimeout this user.")
        

###########################Impregnate###################################

@bot.command()
@commands.cooldown(1, 500, commands.BucketType.user)

async def rat(ctx,):

    Respsones = ['Plague of Vermin','CURSE OF RAT UPON YE']
    Response = random.choice(Respsones)
    await ctx.send(Response)
    
    for _ in range(10):
        try:
            msg = await bot.wait_for("message", timeout=20)
            await msg.add_reaction("🐀")
        except asyncio.TimeoutError:
            await ctx.send( "it is done")
            break

@bot.command()
@commands.cooldown(1, 500, commands.BucketType.user)
async def curse(ctx, member: discord.Member):

    if member.id == 1251700041115238543:
        with open(r'C:\Users\luvlo\Pictures\goku-stare.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
            
    elif member.id == 197119815570161664:
        def check(m):
            return m.author == member and m.channel == ctx.channel
        for _ in range(9):
            try:
                msg = await bot.wait_for("message", check=check, timeout=60)
                await msg.add_reaction("🐀")
            except asyncio.TimeoutError:
                await ctx.send({member.mention}, "it is done")
                break
        
    else:
        await ctx.send(f" Congrats! {member.mention}")

        def check(m):
            return m.author == member and m.channel == ctx.channel

        for _ in range(9):
            try:
                msg = await bot.wait_for("message", check=check, timeout=60)
                await msg.add_reaction("🫃🏿")
            except asyncio.TimeoutError:
                await ctx.send({member.mention}, "it is done")
                break
    
###########################Room Creation####################################
temp_channels = {}

@bot.command()
@commands.cooldown(1, 45, commands.BucketType.user)
async def vc(ctx, *, name: str):
    logChannel = bot.get_channel(1393818188206051419)
    user = ctx.author

    def load_banned_words(filename="BannedWords.txt"):
        try:
            with open(filename, "r") as file:
                return [line.strip().lower() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"[ERROR] {filename} not found.")
            return []

    bannedWords = load_banned_words()

    if any(word in name.lower() for word in bannedWords):
        await logChannel.send(f"❌ {user} ID {user.id} Failed to create temporary voice channel: {name}❌")
        await ctx.send(f"❌{user.mention}, that word is not allowed.")
        return  # Stop here 

    # Get category by ID
    category = ctx.guild.get_channel(1251261508994732102)
    if not category or category.type != discord.ChannelType.category:
        await ctx.send("❌ Could not find the target category.")
        return

    # Create voice channel
    channel = await ctx.guild.create_voice_channel(name, category=category)
    await logChannel.send(f"✅ {user} ID {user.id} Created temporary voice channel: {channel.name}")

    async def monitor_channel():
        await asyncio.sleep(10)
        chan = ctx.guild.get_channel(channel.id)
        if chan and len(chan.members) == 0:
            await chan.delete(reason="Channel was empty for 10 seconds")
            temp_channels.pop(channel.id, None)

    task = asyncio.create_task(monitor_channel())
    temp_channels[channel.id] = task


@bot.event
async def on_voice_state_update(member, before, after):
    # Check if a member left a tracked channel
    if before.channel and before.channel.id in temp_channels:
        chan = before.channel
        await asyncio.sleep(1)  # slight delay to ensure Discord updated state
        if len(chan.members) == 0:
            if not temp_channels[chan.id].done():
                temp_channels[chan.id].cancel()  # cancel any existing countdown
            async def delayed_delete():
                try:
                    await asyncio.sleep(5)
                    if len(chan.members) == 0:
                        await chan.delete(reason="Channel was empty for 30 seconds")
                        temp_channels.pop(chan.id, None)
                except asyncio.CancelledError:
                    pass
            task = asyncio.create_task(delayed_delete())
            temp_channels[chan.id] = task

    # If someone joins a tracked channel, cancel deletion
    if after.channel and after.channel.id in temp_channels:
        if not temp_channels[after.channel.id].done():
            temp_channels[after.channel.id].cancel()

###########################Error handling####################################
@shutdown.error
async def shutdown_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You're not my owner!")

@repeat.error
async def repeat_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You need to be an **admin** to use this command.")


@bot.event
async def on_command_error(ctx, error): #in the case of a price now coming back this will launch
    if isinstance(error, commands.CheckFailure) and ctx.command.name == 'pricecheck':
        await ctx.send("I cannot find the price.")
    else:
        raise error 
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"you cannot use this command right now try again later")
    
    else:
        raise error 

bot.run(TOKEN)
