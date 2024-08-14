import discord
import requests


TOKEN = 'MTE2NjU1OTk1MzM0ODIxODkwMA.GWtjsW.B0djGX-uBsuvdNR4Zo7p_0-DyJbBHnECDgyew4'
CHANNEL_ID = 1189784794867961937  

INTENTS = discord.Intents.default()
INTENTS.message_content = True

client = discord.Client(intents=INTENTS)

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  
        ip_data = response.json()
        return ip_data['ip']
    except requests.RequestException as e:
        print(f"Error fetching IP address: {e}")
        return None

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        ip = get_public_ip()
        if ip:
            await channel.send(f'Bot has logged in. Your public IP address is: {ip}')
        else:
            await channel.send('Bot has logged in, but could not retrieve IP address.')

client.run(TOKEN)
