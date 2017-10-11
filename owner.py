import discord
from discord.ext import commands
import random
import json

class Tags:
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(hidden=True)
	@commands.is_owner()
	async def load(self, ctx, extension_name: str):
		try:
			self.bot.load_extension(extension_name)
		except (AttributeError, ImportError) as e:
			return await ctx.send(f'```py\n{type(e).__name__}: {str(e)}\n```')

		await ctx.send(f'Cog `{extension_name}` loaded successfully.')

	@commands.command(hidden=True)
	@commands.is_owner()
	async def unload(self, ctx, extension_name: str):
		self.bot.unload_extension(extension_name)
		await ctx.send(f'Cog `{extension_name}` has been unloaded.')

	@commands.command(hidden=True)
	@commands.is_owner()
	async def reload(self, ctx, extension_name: str):
		try:
			self.bot.unload_extension(extension_name)
			self.bot.load_extension(extension_name)
		except Exception as e:
			return await ctx.send(f'```py\n{type(e).__name__}: {str(e)}\n```')

		await ctx.send(f'Cog `{extension_name}` has been reloaded.')

def setup(bot):
	bot.add_cog(Tags(bot))