import discord
from discord.ext import commands
import discord.errors
import discord.ext
import sys
import traceback

async def handel_error(bot, ctx, error):
	if isinstance(error, commands.errors.CheckFailure):
		fmt = ":x: Check failure. "
		if isinstance(error, (commands.errors.MissingPermissions, commands.errors.BotMissingPermissions)):
			fmt += str(error)
		await ctx.send(fmt)
	elif isinstance(error, commands.errors.CommandNotFound):
		await ctx.send(":question: Command Not Found")

	print(f'Ignoring exception in command {ctx.command}:', file=sys.stderr)
	traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)