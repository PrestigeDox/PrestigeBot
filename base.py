import discord
from discord.ext import commands
import json
import datetime

class Base:
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(hidden=True, aliases=['pingpong'])
	async def ping(self, ctx):
		pingtime = self.bot.latency * 1000
		pingtimerounded = int(pingtime)
		totalstring = str(pingtimerounded) + 'ms'
		emb = discord.Embed(title='Pong ' + totalstring, colour=0xC500FF)
		await ctx.send(embed=emb)
		#emb = discord.Embed(colour=0xC500FF)
		#emb.add_field(name='Pong!', value='Pong!')


	@commands.command(hidden=True, aliases=['servers'])
	async def stats(self, ctx):
		serverCount = len(self.bot.guilds)
		uptime = (datetime.datetime.now() - self.bot.startuptime)
		hours, rem = divmod(int(uptime.total_seconds()), 3600)
		minutes, seconds = divmod(rem, 60)
		days, hours = divmod(hours, 24)
		time = '%s days, %s hours, %s minutes, and %s seconds' % (days, hours, minutes, seconds)
		users = 0
		pingtime = self.bot.latency * 1000
		pingtimerounded = int(pingtime)
		totalstring = str(pingtimerounded) + 'ms'
		for i in self.bot.get_all_members():
			users = users + 1
		cog_count = len(self.bot.cogs)
		command_count = len(self.bot.commands)
		emb = discord.Embed(colour=0xC500FF)
		emb.add_field(name=' \U0001f550 Uptime', value=time, inline=False)
		emb.add_field(name='Servers \U00002694', value=serverCount, inline=True)
		emb.add_field(name='Ping Time \U0001f3d3', value=totalstring, inline=True)
		emb.add_field(name='Users \U0001f642', value=users, inline=True)
		emb.add_field(name='Cogs \U00002699', value=cog_count, inline=True)
		emb.add_field(name='Commands \U0001f50e', value=command_count, inline=True)
		emb.add_field(name='Messages \U0001f4e5', value=self.bot.messagecounter, inline=True)
		await ctx.send(embed=emb)
		await self.bot.change_presence(game=discord.Game(name=str('On ' + str(serverCount) + ' Servers!')))

	@commands.command(hidden=True, aliases=['info'])
	async def whois(self, ctx, member: discord.Member = None):
		if member == None:
			memberholder = ctx.message.author.id
			member = ctx.guild.get_member(memberholder)
			emb = discord.Embed(colour=0xC500FF)
			emb.set_author(name="Whois for {}".format(member.display_name),
							icon_url=member.avatar_url)
			emb.set_thumbnail(url=member.avatar_url)
			emb.add_field(name="**ID**", value=member.id)
			emb.add_field(name="**Roles**", value=", ".join([r.name for r in member.roles]))
			emb.add_field(name="**Status**", value="**Playing** {}".format(member.game.name if member.game else ""))
			emb.add_field(name="**Color**", value=str(member.color))
			emb.add_field(name="**Joined on**", value=member.joined_at.date())
			emb.add_field(name="**Avatar url**", value="[Here]({})".format(member.avatar_url))
			try:
				await ctx.send(embed=emb)
			except:
				await ctx.send("Too much info...")

		else:
			emb = discord.Embed(colour=0xC500FF)
			emb.set_author(name="Whois for {}".format(member.display_name),
							icon_url=member.avatar_url)
			emb.set_thumbnail(url=member.avatar_url)
			emb.add_field(name="**ID**", value=member.id)
			emb.add_field(name="**Roles**", value=", ".join([r.name for r in member.roles]))
			emb.add_field(name="**Status**", value="**Playing** {}".format(member.game.name if member.game else ""))
			emb.add_field(name="**Color**", value=str(member.color))
			emb.add_field(name="**Joined on**", value=member.joined_at.date())
			emb.add_field(name="**Avatar url**", value="[Here]({})".format(member.avatar_url))
			try:
				await ctx.send(embed=emb)
			except:
				await ctx.send("Too much info...")

	@commands.command(hidden=True, aliases=['serverinfo'])
	async def server(self, ctx):
		membercount = 0
		FAcalc = 0
		for members in ctx.guild.members:
			membercount = membercount + 1
		FAcalc = ctx.guild.mfa_level
		if FAcalc == 1:
			FA = True
		else:
			FA = False
		emb = discord.Embed(colour=0xC500FF)
		emb.set_thumbnail(url=ctx.guild.icon_url)
		emb.add_field(name="Server Name", value=ctx.guild.name)
		emb.add_field(name="Server Owner", value=ctx.guild.owner)
		emb.add_field(name="Server Region", value=ctx.guild.region)
		emb.add_field(name="Member Count", value=membercount)
		emb.add_field(name="Verification Level", value=ctx.guild.verification_level)
		emb.add_field(name="2FA Required", value=FA)
		try:
			await ctx.send(embed=emb)
		except:
			await ctx.send("Too much info...")

	@commands.command(hidden=True, aliases=["setprefix"])
	@commands.has_permissions(administrator=True)
	async def changeprefix(self, ctx, prefix: str = None):
		if str == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='You need to enter a prefix')
			await ctx.send(embed=emb)
		else:
			prefixholderdict = {}
			with open('serverPrefix.json', 'r') as f:
				prefixholderdict = json.load(f)
			prefixholderdict[str(ctx.guild.id)] = prefix
			with open('serverPrefix.json', 'w') as f:
				json.dump(prefixholderdict, f)
			self.bot.prefix_dict[str(ctx.guild.id)] = prefix
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name="New Prefix", value=prefix)
			await ctx.send(embed=emb)

	@commands.command(hidden=True, aliases=['serverprefix', 'serverprefixes'])
	async def prefix(self, ctx):
		holderdictprefix = self.bot.prefix_dict
		serverPrefixVar = holderdictprefix[str(ctx.guild.id)]
		emb = discord.Embed(colour=0xC500FF)
		emb.add_field(name="Server Prefix", value=str(serverPrefixVar))
		await ctx.send(embed=emb)

	@commands.command(hidden=True, aliases=['bot', 'invitebot', 'invitelink', 'botinvitelink', 'botinvite', 'botlink', 'invite', 'link'])
	async def inviteprestige(self, ctx):
		emb = discord.Embed(colour=0xC500FF)
		emb.add_field(name="Bot Invite Link", value='https://discordapp.com/oauth2/authorize?client_id=366268954882211840&scope=bot&permissions=2146958591')
		emb.add_field(name="Support Server", value="https://discord.gg/D6VyHFu")
		await ctx.send(embed=emb)

def setup(bot):
	bot.add_cog(Base(bot))