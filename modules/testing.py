def check(dsc, message):
    if message.content.startswith("!id"):
        dsc.send_message(message.channel, "name " + message.author.name+" id "+message.author.id)
    if message.content.startswith("!chid"):
        dsc.send_message(message.channel, "channel name " + message.channel.name +" id "+message.channel.id)

