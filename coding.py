import discord
from discord.ext import commands
import random
import json
import unicodedata

class Coding:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def charinfo(self, ctx, *, characters: str):
        if len(characters) > 25:
            return await ctx.send(f'Too many characters ({len(characters)}/25)')

        def to_string(c):
            digit = f'{ord(c):x}'
            name = unicodedata.name(c, 'Name not found.')
            return f'`\\U{digit:>08}`: {name} - {c} \N{EM DASH} <http://www.fileformat.info/info/unicode/char/{digit}>'

        await ctx.send('\n'.join(map(to_string, characters)))

def setup(bot):
    bot.add_cog(Coding(bot))