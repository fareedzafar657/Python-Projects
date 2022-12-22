import discord
import random
import os
import requests
import json
from replit import db

TOKEN = "MTA1NDIyODIyMTc3Nzk0NDU3Ng.GovZQb.J-J1RAAJZsY3O7senWfwWMQfJghQiyGqfrKduk"    #practice bot, so there is no need to hide the token

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

sad_words = ["sad", "unhappy", "depressed", "depressing", "awful", "dislike"]

encouraging_words = ["Cheer up!", "Hang in there!", "You are great"]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")  # requests api from this site which is in json format
    json_data = json.loads(response.text)  # loading json file
    quote = json_data[0]["q"] + "   -" + json_data[0][
        "a"]  # this is according to the website like  #[0] is index and ["q"] is key of the dictionary from website api
    return quote

def update_encouragements(encouragement_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.appen(encouragement_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = encouragement_message


@client.event  # reacts to an event #decorator
async def on_ready():
    print(f"Logged in as {client.user}")  # bot call variable with user id


@client.event  # responding to an event
async def on_message(message):  # responds to message
    if message.author == client.user:  # client user is bot like mentioned above
        return
    msg = message.content
    if msg.startswith("!hello"):  # if content of the message starts with it
        await message.channel.send("Hello!")

    if msg.startswith("!inspire"):
        quote = get_quote()  # calls get_quote() function
        await message.channel.send(quote)
    if any(word in msg for word in sad_words):  # comprehenshin fnction and for loop
        await message.channel.send(random.choice(encouraging_words))


client.run(TOKEN)
