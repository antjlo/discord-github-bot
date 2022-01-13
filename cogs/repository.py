import discord
from discord.ext import commands

import requests
import io
import re


class Repository(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def branches(self, ctx, arguments):
        repo_regex = re.compile('^[A-Za-z0-9_-]+/[A-Za-z0-9_-]+$')

        if repo_regex.match(arguments):
            branch_table = requests.get('https://api.github.com/repos/' + arguments + '/branches')
            result = '\n'.join([key['name'] for key in branch_table.json()])

            print(branch_table.status_code)
            await ctx.send(file=discord.File(io.StringIO(result), 'result.txt'))


def setup(bot):
    bot.add_cog(Repository(bot))
