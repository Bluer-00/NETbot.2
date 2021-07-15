import discord
from discord.ext import commands
import asyncio
from io import BytesIO
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=['!', '-'], intents=intents)

@bot.event
async def on_ready():
    activity = discord.Game(name="NET's Discord. Made by Olivergame#8861.", type=3)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="NET's Discord. Made by Olivergame#8861."))
    print("Ready.")

@bot.command()
@commands.has_permissions(administrator=True)
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    try:
        await user.send(message)
        await ctx.send('DM Sent Succesfully.')
    except:
        await ctx.send('User has DMs turned off or blocked the bot.')

        
@bot.event
async def on_member_join(member):
    welcomechannel = bot.get_channel(855184561847009312)
    await welcomechannel.send (f"Hey {member}, welcome to **Stars's Server**!")

@bot.event
async def on_member_remove(member):
    leavechannel = bot.get_channel(855184561847009312)
    await leavechannel.send(f"{member} just left the server.")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')
    
@bot.command()
@commands.has_permissions(administrator=True)
async def staffchange (ctx, *, message):
    await ctx.message.delete()
    channel =bot.get_channel(863376991746523157)
    embed=discord.Embed(title="Staff Change", description = message, color=0x120a8f)
    stafflog = await channel.send(embed=embed)
    await ctx.send(f"{ctx.message.author.mention} - Staff log added to <#863376991746523157>.")
    await stafflog.add_reaction('👍')

@bot.command(pass_context = True)
async def report(ctx, member: discord.Member = None, *, reason = None):
    author = ctx.author

    if member == None:
        await ctx.send('Please mention the user you are reporting after the -report command. EG: -report @user (reason).')
        return
    if reason == None:
        await ctx.send('Please include a reason for the report, after mentioning the user. EG: -report @user (reason).')
        return
    try:
        await asyncio.sleep(1)
        await ctx.message.delete()
        reportschannel=bot.get_channel(863375562017341460)
        await reportschannel.send(f"<@&855178469448089659> The user {ctx.message.author.mention} has reported the user {member.mention}, with the reason of `{reason}`. Please deal with this promptly.")
        await ctx.message.author.send(f"Thanks for making a report {ctx.message.author.mention}. You have reported `{member}`, with the reason of `{reason}`. The staff team have been alerted, and will deal with your report shortly.")
    except:
        await ctx.message.channel.send(f"Thanks for making a report {ctx.message.author.mention}. Your report has been forwarded on to the staff team, however as your DM's are disabled, I'm unable to send you the details of your report via DM's.")
        await ctx.message.delete()
        reportschannel=bot.get_channel(863375562017341460)
        await reportschannel.send(f"<@&855178469448089659> The user {ctx.message.author.mention} has reported the user {member.mention}, with the reason of `{reason}`. Please deal with this promptly.")


adminbancooldown = []

@bot.command(pass_context = True)
@commands.has_any_role('Admin')
async def ban(ctx, member: discord.Member = None, *, reason = None):
    author = ctx.author
    
    if author in adminbancooldown:
        await ctx.send('Please wait.')
        return
    
    if member == None:
        await ctx.send('Please mention a member to ban.')
        return
    if reason == None:
        await ctx.send('Please include a ban reason after the user mention.')
        return
        
    
    try:
        await ctx.send(f'Please wait, processing...')
        await member.send(f'You have been banned from **{ctx.guild.name}** for **{reason}**')
        await asyncio.sleep(1)
        await member.send(f'.\nAs we believe in second chances, you can choose to appeal this punishment. You can either admit to the offence, and potentially be unbanned as we believe in second chances. You can also appeal and claim the ban was unfair or not deserved. To do either of those options, please join our appeals server using the invite below:')
        await asyncio.sleep(1)
        await member.send(f'not including our appeals invite in this sample, add your own here please')
        await asyncio.sleep(1)
        await ctx.send(f'A DM has been sent to the user explaining why they have been banned, now banning the user...')

    except:
        await ctx.send(f'A DM explaining why they have been banned **could not** be sent to the user. The user either has their DM\'s turned off, or has blocked the bot. \n\nProceeding with the ban anyway.')
    await member.ban(reason = f"Banned by {ctx.message.author} for " + reason)
    await asyncio.sleep(3)
    await ctx.send(f'The user has been banned succesfully from the server.')
    punishmentschannel = bot.get_channel(863377485789921290)
    await punishmentschannel.send(f"The user {member.mention} has just been banned by {ctx.message.author.mention}, with the reason of " + reason)
    adminbancooldown.append(author)
    await asyncio.sleep(1)
    adminbancooldown.remove(author)


@bot.command()
@commands.has_permissions(administrator=True)
async def poll (ctx, *, message):
    channel=bot.get_channel(855186229628108820)
    await channel.send("Hey @everyone, there's a new poll! Vote below!")
    embed=discord.Embed(title="New Poll!", description = message, color=0xff00ee)
    await asyncio.sleep(1)
    message = await channel.send(embed=embed)
    await asyncio.sleep(2)
    await message.add_reaction('👍')
    await asyncio.sleep(2)
    await message.add_reaction('👎')

@bot.event
async def on_message_edit(message_before, message_after):
    embed=discord.Embed(title="{} edited a message".format(message_before.author.name), description="", color=0xcdf2f2)
    embed.add_field(name= message_before.content ,value="This is the message before the edit ^^", inline=True)
    embed.add_field(name= message_after.content ,value="This is the message after the edit ^^", inline=True)
    embed.add_field(name= "Credits:" ,value="Message logging and bot coded by Stary1010#8861.", inline=True)
    channel=bot.get_channel(863377485789921290)
    await channel.send(embed=embed)

@bot.event
async def on_message_delete(message):
    embed=discord.Embed(title="{} deleted a message".format(message.author), description=" ", color=0x55246c)
    embed.add_field(name= message.content ,value="Message logging and bot coded by Stary1010#8861.", inline=True)
    channel=bot.get_channel(863377485789921290)
    await channel.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def announce(ctx, *, message=None):
    message = message or "This is an announcement."
    channel=bot.get_channel(855186229628108820)
    await channel.send(message) 
    
@bot.command()
@commands.has_permissions(administrator=True)
async def event(ctx, *, message=None):
    message = message or "This is an event."
    channel=bot.get_channel(822928823044669521)
    await channel.send(message)
    
    
@bot.command()
@commands.has_permissions(administrator=True)
async def partner(ctx, *, message):
    partnerchannel = bot.get_channel(855563232207306753)
    embed=discord.Embed(title="New Partnership!", description=(message), color=0x0085FF)
    partnerembed=await partnerchannel.send(embed=embed)
    pingpong=await partnerchannel.send("@everyone")
    await ctx.send("Sent to <#855563232207306753>")
    await partnerembed.add_reaction('👍')
    await asyncio.sleep(1)
    await pingpong.delete()


cooldown1 = []

@bot.event
async def on_message(message):
    support = bot.get_channel(864232906385129540) 
    if message.channel == support:
        thebot = bot.get_user(860958934374547466) 
        if message.author == thebot:
            return
        guild = message.guild
        await asyncio.sleep(1)
        await message.delete()
        confirmed = await support.send(f"Creating a ticket for {message.author.mention}, please wait.")
        await asyncio.sleep(3)
        await confirmed.delete()
        overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.get_role(855168083832733717): discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_messages=False, attach_files=True),
        guild.get_member(message.author.id): discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_messages=False, attach_files=True)
        }
        channel = await guild.create_text_channel((message.author.name), overwrites=overwrites)
        await asyncio.sleep(1)
        await channel.send(f"Ticket created by {message.author.mention}.")
        await asyncio.sleep(1)
        embed=discord.Embed(title="Issue:", description=(message.content), color=0xff0000)
        await channel.send("You will receive assistance from Staff shortly.")
        await asyncio.sleep(1)
        await channel.send (embed=embed)
        await asyncio.sleep(1)
        ping = await channel.send("<@&855168083832733717> new ticket")
        await asyncio.sleep(5)
        await ping.delete()
        await bot.process_commands(message)

@bot.command()
@commands.has_permissions(administrator=True)
async def close(ctx, channel: discord.TextChannel, theuser: discord.Member=None):
    await ctx.send("Loading transcript, ticket will close shortly.")
    messages = await ctx.channel.history(limit=1000).flatten()
    numbers = "\n".join([f"{message.author}: {message.clean_content}" for message in messages])
    f = BytesIO(bytes(numbers, encoding="utf-8"))
    file = discord.File(fp=f, filename="ticket.txt")
    try:
        await theuser.send("Thank you for using Stars's fan server Support, your support ticket has been closed. Below is your transcript:")
        await asyncio.sleep(0.5)
        await theuser.send(file=file)
    except:
        print("")
    transcriptchannel=bot.get_channel(863379362962472970)
    messages = await ctx.channel.history(limit=1000).flatten()
    numbers = "\n".join([f"{message.author}: {message.clean_content}" for message in messages])
    f = BytesIO(bytes(numbers, encoding="utf-8"))
    file = discord.File(fp=f, filename="ticket.txt")
    await transcriptchannel.send(f"Transcript from {theuser.mention} ticket.")
    await asyncio.sleep(0.5)
    await transcriptchannel.send(file=file)
    await asyncio.sleep(3)
    await channel.delete()

@bot.event
async def on_message(message):
    thechannel = bot.get_channel(862095847298301952)
    if message.channel == thechannel:
        thebot = bot.get_user(864234454885466153)
        if message.author == thebot:
            return
        await thechannel.send(f"<@&864607564410388501>")
    await bot.process_commands(message)

@bot.event
async def on_message(message):
    thechannel = bot.get_channel(862366006864117791)
    if message.channel == thechannel:
        thebot = bot.get_user(864234454885466153)
        if message.author == thebot:
            return
        await thechannel.send(f"<@&864607686498451468>")
    await bot.process_commands(message)

bot.run("ODYwOTU4OTM0Mzc0NTQ3NDY2.YOC0fQ.5MFkokdRO_GDqd6SvtYRCg-vzwA")
