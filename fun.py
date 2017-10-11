import discord
from discord.ext import commands
import random
import json

class Fun:
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(hidden=True, aliases=['coinflip', 'toss', 'cointoss'])
	async def flip(self, ctx):
		choices = ['Heads', 'Tails']
		flip_land = random.choice(choices)
		emb = discord.Embed(colour=0xC500FF)
		emb.add_field(name='Flip Result', value=flip_land)
		await ctx.send(embed=emb)

	@commands.command(hidden=True, aliases=['roll'])
	async def dice(self, ctx, amountDice: int = 1):
		if amountDice > 100:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Dice Amount Can Not Surpass 100')
			await ctx.send(embed=emb)
		elif amountDice == 1:
			dice_roll = random.randint(1,6)
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='Dice Result', value=dice_roll)
			await ctx.send(embed=emb)
		else:
			roll_list = []
			holderint = 0
			for x in range(amountDice):
				roll_list.append(random.randint(1,6))
			for x in roll_list:
				holderint = holderint + int(x)
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='Dice Rolled', value=amountDice, inline=False)
			emb.add_field(name='Roll Values', value=str(roll_list), inline=False)
			emb.add_field(name='Total Value', value=holderint, inline=False)
			await ctx.send(embed=emb)

	@commands.command(hidden=True, name='8ball', aliases=['eball', 'eightball', 'eb'])
	async def _eball(self, ctx, *, question: str = None):
		ball_answers = []
		with open('8ball.json', 'r') as f:
			ball_answers = json.load(f)

		if question == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Yes/No Question Required')
			await ctx.send(embed=emb)
		else:
			emb = discord.Embed(colour=0x0e0f0f)
			emb.set_author(name="8Ball", icon_url="http://emoji.fileformat.info/gemoji/8ball.png")
			emb.add_field(name='Question', value=question, inline=False)
			emb.add_field(name='Answer', value=random.choice(ball_answers), inline=False)
			await ctx.send(embed=emb)

	@commands.command(hidden = True, aliases=['killuser', 'murder'])
	async def kill(self, ctx, user: str = None):
		with open('weapons.json', 'r') as f:
			weapons_list = json.load(f)

		if user == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='User Required')
			await ctx.send(embed=emb)
		else:
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='Killer', value=ctx.author.mention, inline=False)
			emb.add_field(name='Victim', value=user, inline=False)
			emb.add_field(name='Weapon', value=random.choice(weapons_list), inline=False)
			await ctx.send(embed=emb)

	@commands.command(hidden = True)
	async def rate(self, ctx, *, string: str = None):
		if string == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Object to rate is required')
			await ctx.send(embed=emb)
		else:
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='Object to Evaluate', value=string)
			emb.add_field(name='Rating', value=str(random.randint(1,10)) + '/10')
			await ctx.send(embed=emb)


def setup(bot):
	bot.add_cog(Fun(bot))