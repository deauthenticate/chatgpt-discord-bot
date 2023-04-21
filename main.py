import openai, os
import discord
from discord.ext import commands

os.system("cls if os.name == 'nt' else clear")

token = "Authorization | Bot Token Only";

client = commands.Bot(command_prefix = '.', help_command = None, intents=discord.Intents.all())
openai.api_key = "Authorization | OpenAI's API key";

class Chat():
    def __init__(self):
        self.model_id = "gpt-3.5-turbo"

    def get_response(self, *, message):
        self.completion = openai.ChatCompletion.create(
        model=self.model_id,
        messages=[
        {"role": "user", "content": message},
        ]
        )
        return self.completion.choices[0].message.content
    

@client.event
async def on_ready():
    os.system("cls if os.name == 'nt' else clear")
    print("connected; %s" % client.user)
    ok = await client.tree.sync()
    game = discord.Game("exploit#1337")
    await client.change_presence(activity=game, status=discord.Status.idle)

@client.tree.command(description="Get an answer to a question.", name="ask")
async def ask(ctx:discord.Interaction, *, question:str):
    chat = Chat()
    await ctx.response.send_message("Request Sent!")
    try:
        response = chat.get_response(message=question)
    except Exception as e:
        response = "Failed to get response.\n\nDebug info: ```%s```" % e
    # await ctx.send(response)
    em = discord.Embed(description="> %s\n\n```%s```" % (question, response), color=00000)
    em.set_footer(text="Requested by %s" % (ctx.user.name), icon_url=ctx.user.avatar)
    await ctx.channel.send(embed=em)

@client.command()
async def ask(ctx, *, question:str):
    chat = Chat()
    await ctx.send("Request Sent!")
    try:
        response = chat.get_response(message=question)
    except Exception as e:
        response = "Failed to get response.\n\nDebug info: ```%s```" % e
    # await ctx.send(response)
    em = discord.Embed(description="> %s\n\n```%s```" % (question, response), color=00000)
    em.set_footer(text="Requested by %s" % (ctx.author.name), icon_url=ctx.author.avatar)
    await ctx.send(embed=em)

client.run(token, reconnect=True)
