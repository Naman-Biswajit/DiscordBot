from urllib import request
import json
import random

def check(dsc, message):
    if message.content.startswith("!xkcdr"):
        xkcd_get_random(dsc, message)
    if message.content.startswith("!xkcd "):
        num = message.content.split()[1]
        if num.isdigit():
            xkcd_get(dsc, message, num)



def xkcd_get_random(dsc, message):
    xkcd_url = request.urlopen('http://www.xkcd.com/info.0.json')
    xkcd_json = xkcd_url.headers.get_content_charset()
    xkcd_data = json.loads(xkcd_url.read().decode(xkcd_json))
    xkcd_num = xkcd_data['num']
    num = random.randint(1,xkcd_num)
    xkcd_get(dsc, message, num)

def xkcd_get(dsc, message, num):
    xkcd_url = request.urlopen('http://www.xkcd.com/' + str(num) + '/info.0.json')
    xkcd_json = xkcd_url.headers.get_content_charset()
    xkcd_data = json.loads(xkcd_url.read().decode(xkcd_json))
    xkcd_num = xkcd_data['num']
    xkcd_title = xkcd_data['safe_title']
    xkcd_img = xkcd_data['img']
    xkcd_alt = xkcd_data['alt']
    xkcd_msg = "**"+ str(xkcd_num) + "**: " + xkcd_title + " " + xkcd_img + " " + xkcd_alt
    dsc.send_message(message.channel, xkcd_msg)