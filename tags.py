import discord
from discord.ext import commands
import random
import json

class Tags:
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(hidden=True)
	async def setupserver(self, ctx):
		holderdict = {}
		with open('tags.json', 'r') as f:
			prefixdict = json.load(f)
		if str(ctx.guild.id) in prefixdict:
			await ctx.send("Server is already setup")
		else:
			prefixdict[str(ctx.guild.id)] = {}
			prefixdict[str(ctx.guild.id)]['setupleave'] = 'ignore this'
			with open('tags.json', 'w') as f:
				json.dump(prefixdict, f)
			await ctx.send("Tag system setup")

	@commands.command(hidden=True, aliases=['createtag'])
	async def maketag(self, ctx, tagname: str = None, *, tagcontent: str = None):
		prefixdict = {}
		with open('tags.json', 'r') as f:
			prefixdict = json.load(f)
		if tagname == None:
			await ctx.send("Tagname is required")
		elif tagcontent == None:
			await ctx.send("TagContent is required")
		elif tagname in prefixdict[str(ctx.guild.id)]:
			await ctx.send("Tag already Exists")
		else:
			prefixdict[str(ctx.guild.id)][tagname] = tagcontent
			with open('tags.json', 'w') as f:
				json.dump(prefixdict, f)
			await ctx.send("Added tag")

	@commands.command(hidden=True, aliases=['showtag'])
	async def tag(self, ctx, tagname: str = None):
		prefixdict = {}
		with open('tags.json', 'r') as f:
			prefixdict = json.load(f)
		if tagname in prefixdict[str(ctx.guild.id)]:
			await ctx.send(prefixdict[str(ctx.guild.id)][tagname])
		else:
			await ctx.send("Tag doesn't exist")


def setup(bot):
	bot.add_cog(Tags(bot))