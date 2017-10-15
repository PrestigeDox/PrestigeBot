import discord
from discord.ext import commands
import random
import json

class Name:
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(hidden=True)
	@commands.is_owner()
	async def bday(self, ctx, user: discord.Member = None):
		if user == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Name is a required argument')
			await ctx.send(embed=emb)
		else:
			holder = {}
			with open('userbalance.json', 'r') as f:
				holder = json.load(f)
			originalbalance = holder[str(user.id)]["balance"]
			holder[str(user.id)]["balance"] = originalbalance + 1337
			with open('userbalance.json', 'w') as f:
				json.dump(holder, f)
			newbalance = holder[str(user.id)]["balance"]
			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='User', value='\U0001f382 ' + str(user) + ' \U0001f382')
			emb.add_field(name='Message', value='Happy Birthday! We hope you have a great day! If there is anything you need just message Prestige9162. As a small gift we will be transfering you 1337 credits!', inline=False)
			emb.add_field(name='Original Balance', value=str(originalbalance) + ' \U0001f4b3', inline=False)
			emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
			await ctx.send(user.mention)
			await ctx.send(embed=emb)

def setup(bot):
	bot.add_cog(Name(bot))