import discord
from discord.ext import commands
import time

class Admin:
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(hidden=True, aliases=['banuser'])
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, user: discord.Member = None, *, reason: str = None):
		if user == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='@ User Mention is Required')
			await ctx.send(embed=emb)
		elif reason == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Reason for Ban is Required')
			await ctx.send(embed=emb)
		else:
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='User Banned', value=str(user.mention), inline=False)
			emb.add_field(name='Banned By', value=ctx.author.mention, inline=False)
			emb.add_field(name='Ban Reason', value=reason, inline=False)
			await user.ban(delete_message_days=1, reason='Banned by ' + str(ctx.author) + ' and Reason = ' + str(reason))
			await ctx.send(embed=emb)

	@commands.command(hidden=True, aliases=['kickuser'])
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, user: discord.Member = None, *, reason: str = None):
		if user == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='@ User Mention is Required')
			await ctx.send(embed=emb)
		elif reason == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Reason for Kick is Required')
			await ctx.send(embed=emb)
		else:
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='User Kicked', value=str(user.mention), inline=False)
			emb.add_field(name='Kicked By', value=ctx.author.mention, inline=False)
			emb.add_field(name='Kick Reason', value=reason, inline=False)
			await user.kick()
			await ctx.send(embed=emb)

	@commands.command(pass_context=True, hidden=True, aliases=['p'])
	@commands.has_permissions(manage_messages=True)
	async def purge(self, ctx, amount : int = 20):
		amount += 2
		emb = discord.Embed(colour=0xff0c00)
		emb.add_field(name='Status', value='Purging Channel')
		await ctx.send(embed=emb)
		time.sleep(2)
		await ctx.channel.purge(limit=amount)
		emb = discord.Embed(colour=0xff0c00)
		emb.add_field(name='Status', value='Channel Purged', inline=False)
		emb.add_field(name='Messages Removed', value=amount, inline=False)
		await ctx.send(embed=emb)

def setup(bot):
	bot.add_cog(Admin(bot))