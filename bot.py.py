# Simple Google Translate Discord Bot implementation
# Version 1.0
# Author: ethanzs

import discord
from discord.ext import commands
from googletrans import Translator

# Configs
COMMAND_PREFIX = "!"
ON_READY_MESSAGE = "Translate bot is ready."

bot = commands.Bot(command_prefix=COMMAND_PREFIX)
translator = Translator()

# Executed when bot is online
@bot.event
async def on_ready():
    print(ON_READY_MESSAGE)


# Executed when !translate <from> <to> <text> is used on the Discord server
@bot.command()
async def translate(ctx, fro, to, *, text):
    translated = translator.translate(text, src=fro, dest=to)
    await ctx.send(
        "```"
        + fro.capitalize()
        + ": "
        + text
        + "\n"
        + to.capitalize()
        + ": "
        + translated.text
        + "```"
    )


bot.run("PUT SECRET BOT TOKEN HERE")
