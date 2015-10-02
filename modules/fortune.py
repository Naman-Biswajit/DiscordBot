import requests
import json


def check(dsc, message):
    if message.content.startswith("!fort"):
        fortune(dsc, message)


def fortune(dsc, message):
    # TODO: actual fortune cookie, lol
    print(1)
