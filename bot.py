import os
import discord
from textblob import TextBlob
from google_trans_new import google_translator

with open('token.txt', 'r') as token_file:
	TOKEN = token_file.read()
client = discord.Client()
translator = google_translator()

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    await client.change_presence(activity=discord.Game("Litewski fu")) 

@client.event
async def on_message(message):
    if message.author.id != 843230123804065802:
        msg = message.content
        b = TextBlob(msg)
        dupa = b.detect_language()
        print(msg)
        if dupa == 'lt':
            print("lituna")
            translated = translator.translate(msg, lang_tgt='pl', lang_src='lt')
            print(translated)
            embed = CreateEmbed(msg, translated)
            await message.channel.send(embed=embed)

def CreateEmbed(original, translated):
    embed = discord.Embed( 
            title="Lituanski",
        description=f"Jakis lituanin powiedzial cos (Tak wiem ze jestem hujowy to przez api <:troll4k:759121764030087189> )",
        colour=discord.Colour.dark_blue())
    embed.add_field(name=f'Tlumacz: {translated}', value=f'Lituanski: {original}')
    return embed

client.run(TOKEN)
