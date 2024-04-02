import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = ".")

#on ready command
@bot.event
async def on_ready():
    print("Bot is ready")
    await bot.change_presence(activity=discord.Game('Working on code'))

#join/leave commands
@bot.event
async def on_member_join(member):
    print(f'{member} has joined your server :)')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left your server :/')

#bot ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(bot.latency * 1000)}ms')

#8 ball command
@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely', 'You may rely on it.', 'As I see it, yes', 'Most likely', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it.", 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.' ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#purge message(s) command
@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#moderation commands
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

#embed commands
@bot.command()
async def myEmbed(ctx):
    embed = discord.Embed(
        title = 'Inexaura made this!',
        description = 'What description, though?',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text="That's all.")
    #embed.set_image(url=)
    #embed.set_thumbnail(url=)
    #embed.set_author(name='Author Name', icon_url=EmptyEmbed)
    embed.add_field(name='Oh a field!', value='abcde', inline=False)

    emmbed = await ctx.send(embed=embed)
    #await emmbed.add_reaction(':stonks:695745091297476628')

@bot.command()
async def testEmbed(ctx):
    embed = discord.Embed(
        title = 'This is an embed',
        description = 'Testing code',
        colour = discord.Colour.red()
    )

    embed.set_footer(text="Writing my footer text")
    embed.set_thumbnail(url= )
    embed.set_author(name='From inexaura', icon_url= )
    embed.add_field(name=':))', value= "I can write even more text here.")
    embed.add_field(name=':)', value='Hello!', inline=False)

    emmbed = await ctx.send(embed=embed)
    await emmbed.add_reaction(':crownn:697614721817378827')

#command to change bot status
@bot.command()
async def status(ctx, *, status="Currently working on a bot"):
    if ctx.author.id == 429432368454041601:
        await bot.change_presence(activity=discord.Game(status))
    else:
        await ctx.send("Sorry, you don't have access to that command.")

bot.run(key)
