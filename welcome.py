import discord
from discord.ext import commands
import random
import json

class Name:
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.group(invoke_without_command=True, pass_context=True)
	async def welcome(self, ctx):
		emb = discord.Embed(title='\U00002709 Welcome Help', colour=0xC500FF)
		emb.add_field(name='$welcome setup', value='Setup the help command on your server/also use to change the current welcome message', inline=False)
		emb.add_field(name='$welcome check', value='Check if your server is setup/see the welcome message', inline=False)
		await ctx.send(embed=emb)

	@welcome.command(hidden=True)
	async def check(self, ctx):
		holder = {}
		with open('welcome.json', 'r') as f:
			holder = json.load(f)
		if str(ctx.guild.id) in holder:
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='Status', value='Server has already been setup', inline=False)
			await ctx.send(embed=emb)
		else:
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='Status', value='Server has not been setup', inline=False)
			await ctx.send(embed=emb)

	@welcome.command(hidden=True)
	async def setmessage(self, ctx, *, welcome_message: str = None):
		holder = {}
		with open('welcome.json', 'r') as f:
			holder = json.load(f)
		if welcome_message == None:
			embd = discord.Embed(colour=0xff0c00)
			embd.add_field(name='\U0000274c Error', value='Welcome message is required')
			await ctx.send(embed=embd)
		elif '{}' not in welcome_message:
			embd = discord.Embed(colour=0xff0c00)
			embd.add_field(name='\U0000274c Error', value='Welcome message must contain {} for user mention')
			await ctx.send(embed=embd)
		else:
			holder[str(ctx.guild.id)][1] = welcome_message
			with open('welcome.json', 'w') as f:
				holder = json.load(f)
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='Message', value='Message Updated', inline=False)
			await ctx.send(embed=emb)

	@welcome.command(hidden=True)
	async def setchannel(self, ctx, *, welcome_channel: discord.TextChannel = None):
		holder = {}
		with open('welcome.json', 'r') as f:
			holder = json.load(f)
		if welcome_channel == None:
			embd = discord.Embed(colour=0xff0c00)
			embd.add_field(name='\U0000274c Error', value='Welcome channel is required')
			await ctx.send(embed=embd)
		elif str(ctx.guild.id) not in holder:
			print("1) Start of ElIf")
			holder[str(ctx.guild.id)] = []
			print("2) Add server to dict")
			holder[str(ctx.guild.id)][0] = welcome_channel.id
			print("3) Give server channel ID")
			channelid = welcome_channel.id
			with open('welcome.json', 'w') as f:
				holder = json.load(f)
			print("4) Write to file")
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='Message', value=message, inline=False)
			emb.add_field(name='Channel', value=str(channelid), inline=False)
			await ctx.send(embed=emb)
			print("5) Send message")
		else:
			holder[str(ctx.guild.id)][0] = welcome_channel.id
			channelid = welcome_channel.id
			with open('welcome.json', 'w') as f:
				holder = json.load(f)
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='Message', value=message, inline=False)
			emb.add_field(name='Channel', value=str(channelid), inline=False)
			await ctx.send(embed=emb)

def setup(bot):
	bot.add_cog(Name(bot))
