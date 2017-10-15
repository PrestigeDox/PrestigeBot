import discord
from discord.ext import commands
import asyncio
import json
import io
import random
import datetime
import random

import errorhandler

serverPrefix = {}
with open('serverPrefix.json', 'r') as f:
	serverPrefix = json.load(f)

basecogs = ('base', 'admin', 'fun', 'tags', 'owner', 'reminder', 'currency')

async def get_pre(client, message):
	try:
		return serverPrefix.get(str(message.guild.id), "$")
	except:
		default_prefix = "$"
		return default_prefix

bot = commands.Bot(command_prefix=get_pre)
bot.prefix_dict = serverPrefix
bot.startuptime = datetime.datetime.now()
with open('messagecounter.json', 'r') as f:
	mycounterdict = json.load(f)
numholder = mycounterdict["count"]
numholderint = int(numholder)
bot.messagecounter = numholderint
@bot.event
async def on_message(message):
	bot.messagecounter = bot.messagecounter + 1
	print(bot.messagecounter)
	mycounterdict = {}
	with open('messagecounter.json', 'r') as f:
		mycounterdict = json.load(f)
	mycounterdict["count"] = str(bot.messagecounter)
	with open('messagecounter.json', 'w') as f:
		json.dump(mycounterdict, f)
	await bot.process_commands(message)

@bot.event
async def on_ready():
	print("Bot Online!")
	print("Name: {}".format(bot.user.name))
	print("ID: {}".format(bot.user.id))
	print(discord.__version__)
	for x in basecogs:
		bot.load_extension(x)

@bot.event
async def on_command_error(ctx: commands.Context, err):
    if hasattr(ctx.command, "on_error"):
        return
    await errorhandler.handel_error(bot, ctx, err)

@bot.event
async def on_guild_join(nameGuild):
	prefixholderdict = {}
	with open('serverPrefix.json', 'r') as f:
		prefixholderdict = json.load(f)
	prefixholderdict[str(nameGuild.id)] = "$"
	with open('serverPrefix.json', 'w') as f:
		json.dump(prefixholderdict, f)
	holderdict = {}
	with open('tags.json', 'r') as f:
		holderdict = json.load(f)
	holderdict[str(ctx.guild.id)] = [{"FirstTagEver": {"author_id": "350534218998349825", "content": "This Server's First Every Tag", "aliases": [], "uses": "2"}}]
	with open('tags.json', 'w') as f:
		json.dump(holderdict, f)

bot.run("TOKEN")
