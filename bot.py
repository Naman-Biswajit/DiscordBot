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


discord_client.run()
