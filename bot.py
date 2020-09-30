import discord
import json
import pprint
# import module for settings generation
import modules.config_gen
# import bot modules. TODO: maybe dynamic loading?
import modules.admin
import modules.testing
import modules.xkcd
import modules.fortune

# connecting to APIs



def load_config():
    try:
        print('Loading settings')
        with open('config.json') as data_file:
            config = json.load(data_file)

    except:
        modules.config_gen.create_json()
        config = load_config()

    return config

# initialize

config = load_config()

print('Connecting to API')
discord_client = discord.Client()

try:
    print(config["discord"]["email"])
    print(config["discord"]["password"])
    discord_client.login(config["discord"]["email"], config["discord"]["password"])
except:
    print('Cannot connect to Discord')


# EVENTS


@discord_client.event
def on_ready():
    print('Logged in as')
    print(discord_client.user.name)
    print(discord_client.user.id)
    print('------')


@discord_client.event
def on_message(message):
    if discord_client.user.id != message.author.id:
        modules.testing.check(discord_client, message)
        modules.xkcd.check(discord_client, message)
        modules.fortune.check(discord_client, message)

@discord_client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(discord_client.latency * 1000)}')

@discord_client.command()
async def kick(ctx, member: discord.Member, *, arg='Not provided'):
    await member.kick(reason=arg)
    await ctx.send(f'{member.mention} has been kick by {ctx.author.mention}. reason: {arg}')

@discord_client.command()
async def ban(ctx, member: discord.Member, *, arg='Not provided'):
    await member.ban(reason=arg)
    await ctx.send(f'{member.mention} has been banned by {ctx.author.mention}. reason: {arg}')

@discord_client.command()
async def kick(ctx, member: discord.Member, *, arg):
    await member.kick(reason=arg)

@discord_client.command()
@commands.has_permissions(ban_members=True)
async def unban(self, ctx, member: discord.Object):
    await ctx.guild.unban(member)
    await ctx.send(f'Ok unbanned user with ID {member.id}')

@discord_client.command()
async def clear(self, ctx, amount):
    total = await ctx.channel.purge(limit=amount)
    await ctx.send('done', delete_after=4)

@discord_client.command()
@commands.has_guild_permissions(mute_members=True)
async def mute(self, ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild

    for role in guild.roles:
        if role.name in ['muted', 'Muted']:
            await member.add_roles(role, reason=reason)
            await ctx.send(f'{member.mention} has been muted by {ctx.author.mention}')
            return

    overwrite = discord.PermissionOverwrite(send_messages=False)
    newRole = await guild.create_role(name='Muted')

    for channel in guild.text_channels:
        await channel.set_permissions(newRole, overwrite=overwrite)

    await member.add_roles(newRole)
    await ctx.send(f'{member.mention} has been muted by {ctx.author.mention}')

@discord_client.command()
@commands.has_guild_permissions(mute_members=True)
async def unmute(self, ctx, member: discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name in ['muted', 'Muted']:
            try:
                await member.remove_roles(role)
            except:  
                await ctx.send('member is already unmuted')
                return

            await ctx.send(f'{member.mention} has been unmuted by {ctx.author.mention}')
            return

    await ctx.send('Muted role not found')

discord_client.run()