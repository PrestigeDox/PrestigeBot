import discord
from discord.ext import commands
import random
import json
import time
import random
import asyncio
import time

class Currency:
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(hidden=True, aliases=['dailyclaim', 'claim', 'dailybalance', 'atmclaim'])
	async def daily(self, ctx):
		userinfo = {}
		with open('userbalance.json', 'r') as f:
			userinfo = json.load(f)
		if str(ctx.author.id) not in userinfo:
			userinfo[str(ctx.author.id)] = {}
			userinfo[str(ctx.author.id)]["balance"] = 250
			userinfo[str(ctx.author.id)]["lastclaimed"] = time.time()
			balance = userinfo[str(ctx.author.id)]["balance"]
			with open('userbalance.json', 'w') as f:
				json.dump(userinfo, f)
			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='Amount Claimed', value="250 \U0001f4b3", inline=False)
			emb.add_field(name='Balance', value=str(balance) + ' \U0001f4b3', inline=False)
			await ctx.send(embed=emb)
		elif str(ctx.author.id) in userinfo:
			timesince = userinfo[str(ctx.author.id)]["lastclaimed"] + 86400
			if timesince < time.time():
				initialbalance = userinfo[str(ctx.author.id)]["balance"]
				newbalance = initialbalance + 250
				userinfo[str(ctx.author.id)]["balance"] = newbalance
				userinfo[str(ctx.author.id)]["lastclaimed"] = time.time()
				with open('userbalance.json', 'w') as f:
					json.dump(userinfo, f)
				balance = userinfo[str(ctx.author.id)]["balance"]
				emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
				emb.add_field(name='Amount Claimed', value="250 \U0001f4b3", inline=False)
				emb.add_field(name='Balance', value=str(balance) + ' \U0001f4b3', inline=False)
				await ctx.send(embed=emb)
			else:
				balance = userinfo[str(ctx.author.id)]["balance"]
				timeclaimed = userinfo[str(ctx.author.id)]["lastclaimed"]
				timems = 0
				timems = timeclaimed + 86400
				timefinal = 0
				timefinal = timems - time.time()
				timehours = 0
				timehours = timefinal / 3600
				timeminutes = 0
				timehold = 0

				timehold = timefinal % 3600
				timeminutes = timehold / 60

				timefinalhours = int(timehours)
				timefinalminutes = int(timeminutes)

				if timefinalhours < 1:
					timefinalhours = 0

				if timefinalminutes < 1:
					timefinalminutes = 0
				emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
				emb.add_field(name='Next Claim For User', value=str(timefinalhours) + 'H ' + str(timefinalminutes) + 'M', inline=False)
				await ctx.send(embed=emb)

	@commands.command(hidden=True, aliases=['currentbalance', 'bal'])
	async def balance(self, ctx, accountID: discord.Member = None):
		userinfo = {}
		with open('userbalance.json', 'r') as f:
			userinfo = json.load(f)
		if accountID == None:
			'''
			So.... Over here you see loads of jumble... if you don't like it... well...
			I don't really give a shit.... I'm crap with numbers and you need to  get used to it...
			Numbers in jumble... Well expect it in my code
			'''
			balance = userinfo[str(ctx.author.id)]["balance"]
			timeclaimed = userinfo[str(ctx.author.id)]["lastclaimed"]
			timems = 0
			timems = timeclaimed + 86400
			timefinal = 0
			timefinal = timems - time.time()
			timehours = 0
			timehours = timefinal / 3600
			timeminutes = 0
			timehold = 0

			timehold = timefinal % 3600
			timeminutes = timehold / 60

			timefinalhours = int(timehours)
			timefinalminutes = int(timeminutes)

			if timefinalhours < 1:
				timefinalhours = 0

			if timefinalminutes < 1:
				timefinalminutes = 0

			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='Balance', value=str(balance) + ' \U0001f4b3', inline=False)
			emb.add_field(name='Next Claim', value=str(timefinalhours) + 'H ' + str(timefinalminutes) + 'M', inline=False)
			await ctx.send(embed=emb)
		else:
			try:
				balance = userinfo[str(accountID.id)]["balance"]
				timeclaimed = userinfo[str(accountID.id)]["lastclaimed"]
				timems = 0
				timems = timeclaimed + 86400
				timefinal = 0
				timefinal = timems - time.time()
				timehours = 0
				timehours = timefinal / 3600
				timeminutes = 0
				timehold = 0

				timehold = timefinal % 3600
				timeminutes = timehold / 60

				timefinalhours = int(timehours)
				timefinalminutes = int(timeminutes)

				if timefinalhours < 1:
					timefinalhours = 0

				if timefinalminutes < 1:
					timefinalminutes = 0

				emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
				emb.add_field(name='User', value=accountID)
				emb.add_field(name='Balance', value=str(balance) + ' \U0001f4b3', inline=False)
				emb.add_field(name='Next Claim', value=str(timefinalhours) + 'H ' + str(timefinalminutes) + 'M', inline=False)
				await ctx.send(embed=emb)
			except:
				emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
				emb.add_field(name='Create Account', value="The user doesn't have an account but can easily create one via claiming their daily reward. Simply run the command $daily (change the prefix to the relevant server prefix!")
				await ctx.send(embed=emb)

	@commands.command(hidden=True, aliases=['haxor', 'haxthesystem', 'cheat', 'cheatcode', '1337leet', '1337leethaxor', '1337haxor', '1337haxorgive'])
	@commands.is_owner()
	async def haxorsomep(self, ctx, user: discord.Member, amount: int = None):
		holder = {}
		if amount == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Amount is a required argument')
			await ctx.send(embed=emb)
		with open('userbalance.json', 'r') as f:
			holder = json.load(f)
		if str(user.id) not in holder:
			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='Create Account', value="The user doesn't have an account but can easily create one via claiming their daily reward. Simply run the command $daily (change the prefix to the relevant server prefix!")
			await ctx.send(embed=emb)
		else:
			originalbalance = holder[str(user.id)]["balance"]
			holder[str(user.id)]["balance"] = originalbalance + amount
			with open('userbalance.json', 'w') as f:
				json.dump(holder, f)
			newbalance = holder[str(user.id)]["balance"]
			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='User', value=user)
			emb.add_field(name='Original Balance', value=str(originalbalance) + ' \U0001f4b3', inline=False)
			emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
			await ctx.send(embed=emb)

	@commands.command(hidden=True, aliases=['haxordel', 'haxthesystemdel', 'cheatdel', 'cheatcodedel', '1337leetdel', '1337leethaxordel', '1337haxordel', '1337haxorgivedel'])
	@commands.is_owner()
	async def haxorsomepdel(self, ctx, user: discord.Member, amount: int = None):
		holder = {}
		if amount == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Amount is a required argument')
			await ctx.send(embed=emb)
		with open('userbalance.json', 'r') as f:
			holder = json.load(f)
		if str(user.id) not in holder:
			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='Create Account', value="The user doesn't have an account but can easily create one via claiming their daily reward. Simply run the command $daily (change the prefix to the relevant server prefix!")
			await ctx.send(embed=emb)
		else:
			originalbalance = holder[str(user.id)]["balance"]
			holder[str(user.id)]["balance"] = originalbalance - amount
			with open('userbalance.json', 'w') as f:
				json.dump(holder, f)
			newbalance = holder[str(user.id)]["balance"]
			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='User', value=user)
			emb.add_field(name='Original Balance', value=str(originalbalance) + ' \U0001f4b3', inline=False)
			emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
			await ctx.send(embed=emb)

	@commands.group(invoke_without_command=True, pass_context=True)
	async def fish(self, ctx):
		emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
		emb.add_field(name='$fish sell', value='Look at your inventory and see what you can sell', inline=False)
		emb.add_field(name='$fish catch', value='Spend 10 \U0001f4b3 to catch fish', inline=False)
		await ctx.send(embed=emb)

	@fish.command(hidden=True)
	async def catch(self, ctx):
		holder = {}
		with open('userbalance.json', 'r') as f:
			holder = json.load(f)
		balance = holder[str(ctx.author.id)]["balance"]
		if balance < 10:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value="Balance is less than 10 \U0001f4b3")
			await ctx.send(embed=emb)
		else:
			newbalance = balance - 10
			holder[str(ctx.author.id)]["balance"] = newbalance
			with open('userbalance.json', 'w') as f:
				json.dump(holder, f)
			catch = ['fish', 'fish', 'fish', 'fish', 'fish', 'fish', 'fish', 'fish', 'tropicalfish', 'fishcake', 'fishcake', 'blowfish', 'blowfish', 'paperclip', 'paperclip', 'paperclip', 'skull', 'skull', 'skull']
			finalcatch = random.choice(catch)
			fish = {}
			with open('fish.json', 'r') as f:
				fish = json.load(f)
			if str(ctx.author.id) not in fish:
				fish[str(ctx.author.id)] = {"fish": 0, "tropicalfish": 0, "fishcake": 0, "blowfish": 0, "paperclip": 0, "skull": 0}
				if finalcatch == 'fish':
					emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
					emb.add_field(name='Your Catch', value='\U0001f41f', inline=False)
					emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
					await ctx.send(embed=emb)
					newcount = fish[str(ctx.author.id)]["fish"] + 1
					fish[str(ctx.author.id)]["fish"] = newcount
					with open('fish.json', 'w') as f:
						json.dump(fish, f)
				elif finalcatch == 'tropicalfish':
					emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
					emb.add_field(name='Your Catch', value='\U0001f420', inline=False)
					emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
					await ctx.send(embed=emb)
					newcount = fish[str(ctx.author.id)]["tropicalfish"] + 1
					fish[str(ctx.author.id)]["tropicalfish"] = newcount
					with open('fish.json', 'w') as f:
						json.dump(fish, f)
				elif finalcatch == 'fishcake':
					emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
					emb.add_field(name='Your Catch', value='\U0001f365', inline=False)
					emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
					await ctx.send(embed=emb)
					newcount = fish[str(ctx.author.id)]["fishcake"] + 1
					fish[str(ctx.author.id)]["fishcake"] = newcount
					with open('fish.json', 'w') as f:
						json.dump(fish, f)
				elif finalcatch == 'blowfish':
					emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
					emb.add_field(name='Your Catch', value='\U0001f421', inline=False)
					emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
					await ctx.send(embed=emb)
					newcount = fish[str(ctx.author.id)]["blowfish"] + 1
					fish[str(ctx.author.id)]["blowfish"] = newcount
					with open('fish.json', 'w') as f:
						json.dump(fish, f)
				elif finalcatch == 'paperclip':
					emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
					emb.add_field(name='Your Catch', value='\U0001f4ce', inline=False)
					emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
					await ctx.send(embed=emb)
					newcount = fish[str(ctx.author.id)]["paperclip"] + 1
					fish[str(ctx.author.id)]["paperclip"] = newcount
					with open('fish.json', 'w') as f:
						json.dump(fish, f)
				elif finalcatch == 'skull':
					emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
					emb.add_field(name='Your Catch', value='\U0001f480', inline=False)
					emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
					await ctx.send(embed=emb)
					newcount = fish[str(ctx.author.id)]["skull"] + 1
					fish[str(ctx.author.id)]["skull"] = newcount
					with open('fish.json', 'w') as f:
						json.dump(fish, f)
			else:
				if finalcatch == 'fish':
					emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
					emb.add_field(name='Your Catch', value='\U0001f41f', inline=False)
					emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
					await ctx.send(embed=emb)
					newcount = fish[str(ctx.author.id)]["fish"] + 1
					fish[str(ctx.author.id)]["fish"] = newcount
					with open('fish.json', 'w') as f:
						json.dump(fish, f)
				elif finalcatch == 'tropicalfish':
					emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
					emb.add_field(name='Your Catch', value='\U0001f420', inline=False)
					emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
					await ctx.send(embed=emb)
					newcount = fish[str(ctx.author.id)]["tropicalfish"] + 1
					fish[str(ctx.author.id)]["tropicalfish"] = newcount
					with open('fish.json', 'w') as f:
						json.dump(fish, f)
				elif finalcatch == 'fishcake':
					emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
					emb.add_field(name='Your Catch', value='\U0001f365', inline=False)
					emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
					await ctx.send(embed=emb)
					newcount = fish[str(ctx.author.id)]["fishcake"] + 1
					fish[str(ctx.author.id)]["fishcake"] = newcount
					with open('fish.json', 'w') as f:
						json.dump(fish, f)
				elif finalcatch == 'blowfish':
					emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
					emb.add_field(name='Your Catch', value='\U0001f421', inline=False)
					emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
					await ctx.send(embed=emb)
					newcount = fish[str(ctx.author.id)]["blowfish"] + 1
					fish[str(ctx.author.id)]["blowfish"] = newcount
					with open('fish.json', 'w') as f:
						json.dump(fish, f)
				elif finalcatch == 'paperclip':
					emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
					emb.add_field(name='Your Catch', value='\U0001f4ce', inline=False)
					emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
					await ctx.send(embed=emb)
					newcount = fish[str(ctx.author.id)]["paperclip"] + 1
					fish[str(ctx.author.id)]["paperclip"] = newcount
					with open('fish.json', 'w') as f:
						json.dump(fish, f)
				elif finalcatch == 'skull':
					emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
					emb.add_field(name='Your Catch', value='\U0001f480', inline=False)
					emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
					await ctx.send(embed=emb)
					newcount = fish[str(ctx.author.id)]["skull"] + 1
					fish[str(ctx.author.id)]["skull"] = newcount
					with open('fish.json', 'w') as f:
						json.dump(fish, f)

	@fish.command(hidden=True, aliases=['inv', 'invent', 'supply', 'stock', 'sell'])
	async def inventory(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		holder = {}
		with open('fish.json', 'r') as f:
			holder = json.load(f)

		emote_tuple = ('\U0001f41f',
					   '\U0001f420',
					   '\U0001f365',
					   '\U0001f421',
					   '\U0001f4ce',
					   '\U0001f480')

		if user == None:
			fish = holder[str(ctx.author.id)]["fish"]
			tropicalfish = holder[str(ctx.author.id)]["tropicalfish"]
			fishcake = holder[str(ctx.author.id)]["fishcake"]
			blowfish = holder[str(ctx.author.id)]["blowfish"]
			paperclip = holder[str(ctx.author.id)]["paperclip"]
			skull = holder[str(ctx.author.id)]["skull"]
			emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
			emb.add_field(name='Amount of \U0001f41f', value=fish, inline=False)
			emb.add_field(name='Amount of \U0001f420', value=tropicalfish, inline=False)
			emb.add_field(name='Amount of \U0001f365', value=fishcake, inline=False)
			emb.add_field(name='Amount of \U0001f421', value=blowfish, inline=False)
			emb.add_field(name='Amount of \U0001f4ce', value=paperclip, inline=False)
			emb.add_field(name='Amount of \U0001f480', value=skull, inline=False)
			bot_message = await ctx.send(embed=emb, delete_after=300)
			for x in emote_tuple:
				await bot_message.add_reaction(x)
			def check(reaction, user):
				return user == ctx.author and reaction.emoji in emote_tuple and reaction.message.id == bot_message.id
			while True:
				print("LOOP")
				try:
					reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=300.0)
				except asyncio.TimeoutError:
					return await bot_message.clear_reactions()
				balanceholder = {}
				if reaction.emoji == '\U0001f41f':
					print("1 Detected that emoji is fish")
					if holder[str(ctx.author.id)]["fish"] > 0:
						#Edit fish name above
						myholdercounter = holder[str(ctx.author.id)]["fish"] - 1
						print(holder[str(ctx.author.id)]["fish"])
						print(myholdercounter)
						print("2 -1 counter")
						#Edit fish name above
						holder[str(ctx.author.id)]["fish"] = myholdercounter
						print(holder)
						print("3 add new val to dict")
						#Edit fish name above
						with open('fish.json', 'w') as f:
							json.dump(holder, f)
						print("4 Upload new dict to JSON")
						with open('userbalance.json', 'r') as f:
							balanceholder = json.load(f)
						print("5 Reading JSON balance")
						userbalance = balanceholder[str(ctx.author.id)]["balance"]
						userbalance = userbalance + 10
						print("6 Adding bal to variable")
						#Edit fish value above
						balanceholder[str(ctx.author.id)]["balance"] = userbalance
						with open('userbalance.json', 'w') as f:
							json.dump(balanceholder, f)
						print("7 New Val to JSON")
						emb.set_field_at(0, name='Amount of \U0001f41f', value=myholdercounter, inline=False)
						print("8 Set new embed field")
						#Edit fish name above fish-1
						await bot_message.edit(embed=emb)
						print("9 Edit Embed")
						await bot_message.remove_reaction('\U0001f41f', ctx.author)
						print("10 Remove user reaction")
						embp = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xFFD700)
						embp.add_field(name='Sale', value='10 \U0001f4b3 added to your balance!')
						await ctx.send(embed=embp, delete_after=60)
					else:
						embd = discord.Embed(colour=0xff0c00)
						embd.add_field(name='\U0000274c Error', value='The value of that item in your inv is 0')
						await ctx.send(embed=embd)
				elif reaction.emoji == '\U0001f420':
					if holder[str(ctx.author.id)]["tropicalfish"] > 0:
						#Edit fish name above
						myholdercounter = holder[str(ctx.author.id)]["tropicalfish"] - 1
						#Edit fish name above
						holder[str(ctx.author.id)]["tropicalfish"] = myholdercounter
						#Edit fish name above
						with open('fish.json', 'w') as f:
							json.dump(holder, f)
						with open('userbalance.json', 'r') as f:
							balanceholder = json.load(f)
						userbalance = balanceholder[str(ctx.author.id)]["balance"]
						userbalance = userbalance + 25
						#Edit fish value above
						balanceholder[str(ctx.author.id)]["balance"] = userbalance
						with open('userbalance.json', 'w') as f:
							json.dump(balanceholder, f)
						emb.set_field_at(1, name='Amount of \U0001f420', value=myholdercounter, inline=False)
						#Edit fish name above fish-1
						await bot_message.edit(embed=emb)
						await bot_message.remove_reaction('\U0001f420', ctx.author)
						embp = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xFFD700)
						embp.add_field(name='Sale', value='10 \U0001f4b3 added to your balance!')
						await ctx.send(embed=embp, delete_after=60)
					else:
						embd = discord.Embed(colour=0xff0c00)
						embd.add_field(name='\U0000274c Error', value='The value of that item in your inv is 0')
						await ctx.send(embed=embd)
				elif reaction.emoji == '\U0001f365':
					if holder[str(ctx.author.id)]["fishcake"] > 0:
						#Edit fish name above
						myholdercounter = holder[str(ctx.author.id)]["fishcake"] - 1
						#Edit fish name above
						holder[str(ctx.author.id)]["fishcake"] = myholdercounter
						#Edit fish name above
						with open('fish.json', 'w') as f:
							json.dump(holder, f)
						with open('userbalance.json', 'r') as f:
							balanceholder = json.load(f)
						userbalance = balanceholder[str(ctx.author.id)]["balance"]
						userbalance = userbalance + 15
						#Edit fish value above
						balanceholder[str(ctx.author.id)]["balance"] = userbalance
						with open('userbalance.json', 'w') as f:
							json.dump(balanceholder, f)
						emb.set_field_at(2, name='Amount of \U0001f365', value=myholdercounter, inline=False)
						#Edit fish name above fish-1
						await bot_message.edit(embed=emb)
						await bot_message.remove_reaction('\U0001f365', ctx.author)
						embp = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xFFD700)
						embp.add_field(name='Sale', value='10 \U0001f4b3 added to your balance!')
						await ctx.send(embed=embp, delete_after=60)
					else:
						embd = discord.Embed(colour=0xff0c00)
						embd.add_field(name='\U0000274c Error', value='The value of that item in your inv is 0')
						await ctx.send(embed=embd)
				elif reaction.emoji == '\U0001f421':
					if holder[str(ctx.author.id)]["blowfish"] > 0:
						#Edit fish name above
						myholdercounter = holder[str(ctx.author.id)]["blowfish"] - 1
						#Edit fish name above
						holder[str(ctx.author.id)]["blowfish"] = myholdercounter
						#Edit fish name above
						with open('fish.json', 'w') as f:
							json.dump(holder, f)
						with open('userbalance.json', 'r') as f:
							balanceholder = json.load(f)
						userbalance = balanceholder[str(ctx.author.id)]["balance"]
						userbalance = userbalance + 30
						#Edit fish value above
						balanceholder[str(ctx.author.id)]["balance"] = userbalance
						with open('userbalance.json', 'w') as f:
							json.dump(balanceholder, f)
						emb.set_field_at(3, name='Amount of \U0001f421', value=myholdercounter, inline=False)
						#Edit fish name above fish-1
						await bot_message.edit(embed=emb)
						await bot_message.remove_reaction('\U0001f421', ctx.author)
						embp = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xFFD700)
						embp.add_field(name='Sale', value='10 \U0001f4b3 added to your balance!')
						await ctx.send(embed=embp, delete_after=60)
					else:
						embd = discord.Embed(colour=0xff0c00)
						embd.add_field(name='\U0000274c Error', value='The value of that item in your inv is 0')
						await ctx.send(embed=embd)
				elif reaction.emoji == '\U0001f4ce':
					if holder[str(ctx.author.id)]["paperclip"] > 0:
						#Edit fish name above
						myholdercounter = holder[str(ctx.author.id)]["paperclip"] - 1
						#Edit fish name above
						holder[str(ctx.author.id)]["paperclip"] = myholdercounter
						#Edit fish name above
						with open('fish.json', 'w') as f:
							json.dump(holder, f)
						with open('userbalance.json', 'r') as f:
							balanceholder = json.load(f)
						userbalance = balanceholder[str(ctx.author.id)]["balance"]
						userbalance = userbalance + 5
						#Edit fish value above
						balanceholder[str(ctx.author.id)]["balance"] = userbalance
						with open('userbalance.json', 'w') as f:
							json.dump(balanceholder, f)
						emb.set_field_at(4, name='Amount of \U0001f4ce', value=myholdercounter, inline=False)
						#Edit fish name above fish-1
						await bot_message.edit(embed=emb)
						await bot_message.remove_reaction('\U0001f4ce', ctx.author)
						embp = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xFFD700)
						embd.add_field(name='Sale', value='10 \U0001f4b3 added to your balance!')
						await ctx.send(embed=embp, delete_after=60)
					else:
						embd = discord.Embed(colour=0xff0c00)
						embp.add_field(name='\U0000274c Error', value='The value of that item in your inv is 0')
						await ctx.send(embed=embd)
				elif reaction.emoji == '\U0001f480':
					if holder[str(ctx.author.id)]["skull"] > 0:
						#Edit fish name above
						myholdercounter = holder[str(ctx.author.id)]["skull"] - 1
						#Edit fish name above
						holder[str(ctx.author.id)]["skull"] = myholdercounter
						#Edit fish name above
						with open('fish.json', 'w') as f:
							json.dump(holder, f)
						with open('userbalance.json', 'r') as f:
							balanceholder = json.load(f)
						userbalance = balanceholder[str(ctx.author.id)]["balance"]
						userbalance = userbalance + 5
						#Edit fish value above
						balanceholder[str(ctx.author.id)]["balance"] = userbalance
						with open('userbalance.json', 'w') as f:
							json.dump(balanceholder, f)
						emb.set_field_at(5, name='Amount of \U0001f480', value=myholdercounter, inline=False)
						#Edit fish name above fish-1
						await bot_message.edit(embed=emb)
						await bot_message.remove_reaction('\U0001f480', ctx.author)
						embp = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xFFD700)
						embp.add_field(name='Sale', value='10 \U0001f4b3 added to your balance!')
						await ctx.send(embed=embp, delete_after=60)
					else:
						embd = discord.Embed(colour=0xff0c00)
						embd.add_field(name='\U0000274c Error', value='The value of that item in your inv is 0')
						await ctx.send(embed=embd)

		else:
			fish = holder[str(user.id)]["fish"]
			tropicalfish = holder[str(user.id)]["tropicalfish"]
			fishcake = holder[str(user.id)]["fishcake"]
			blowfish = holder[str(user.id)]["blowfish"]
			paperclip = holder[str(user.id)]["paperclip"]
			skull = holder[str(user.id)]["skull"]
			emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
			emb.add_field(name='User', value=user, inline=False)
			emb.add_field(name='Amount of \U0001f41f', value=fish, inline=False)
			emb.add_field(name='Amount of \U0001f420', value=tropicalfish, inline=False)
			emb.add_field(name='Amount of \U0001f365', value=fishcake, inline=False)
			emb.add_field(name='Amount of \U0001f421', value=blowfish, inline=False)
			emb.add_field(name='Amount of \U0001f4ce', value=paperclip, inline=False)
			emb.add_field(name='Amount of \U0001f480', value=skull, inline=False)
			await ctx.send(embed=emb, delete_after=300)

	@commands.command(hidden=True)
	async def slots(self, ctx, bet: int = None):
		if bet == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Bet is a required argument')
			await ctx.send(embed=emb)
		elif bet < 1:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Bet is required to be a positive number')
			await ctx.send(embed=emb)
		else:
			#In progress
			pass

def setup(bot):
	bot.add_cog(Currency(bot))