import discord
from discord.ext import commands
import random
import json
import asyncio

class Reminder:
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(aliases=['remindme'])
	async def remind(self, ctx, time_in_minutes: int, *, message: str):
		emb = discord.Embed(colour=0xC500FF)
		emb.add_field(name='User', value=ctx.message.author.mention, inline=False)
		emb.add_field(name='New Reminder', value=message, inline=False)
		emb.add_field(name='Time Till', value=str(time_in_minutes) + ' Minutes', inline=False)
		await ctx.send(embed=emb)
		await asyncio.sleep(time_in_minutes * 60)
		try:
			emb = discord.Embed(title='\U0001f6a8 Reminder \U0001f6a8', colour=0xC500FF)
			emb.add_field(name='Message', value=message, inline=False)
			emb.add_field(name='Time Waited', value=time_in_minutes, inline=False)
			await ctx.author.send(ctx.author.mention)
			await ctx.author.send(embed=emb)
		except discord.Forbidden:
			emb = discord.Embed(title='\U0001f6a8 Reminder \U0001f6a8', colour=0xC500FF)
			emb.add_field(name='Message', value=message, inline=False)
			emb.add_field(name='Time Waited', value=time_in_minutes, inline=False)
			await ctx.send(ctx.author.mention)
			await ctx.send(embed=emb)

def setup(bot):
	bot.add_cog(Reminder(bot))