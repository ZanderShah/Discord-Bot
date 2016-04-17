import discord
import asyncio
import random
import wolframalpha

client = discord.Client()
mathGod = wolframalpha.Client(input())

#https://discordapp.com/oauth2/authorize?client_id=171079718131466240&scope=bot&permissions=66186303

async def math(message, query):
    res = mathGod.query(query)
    for pod in res.pods:
        if pod.text != query and pod.text != None and pod.text != '(data not available)':
            await client.send_message(message.channel, pod.text)
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('.test'):
        await client.send_message(message.channel, 'Works!');
    elif message.content.startswith('.sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('.roll'):
        upper = 101
        if message.content.startswith('.roll ') and message.content[6:].isdigit():
            upper = int(message.content[6:])
        await client.send_message(message.channel, random.randrange(1, upper, 1))
    elif message.content.startswith('.hello'):
        await client.send_message(message.channel, 'Hello, {0}'.format(message.author))
    elif message.content.startswith('.math '):
        await math(message, message.content[6:])
    elif message.content.startswith('.help'):
        await client.send_message(message.channel, 'I can\'t help you')
    elif message.content.startswith('.ay'):
        await client.send_message(message.channel, 'Ayyyyyyyyy')

client.run(input())
