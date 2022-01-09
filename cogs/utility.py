import discord
from discord.ext import commands

import requests


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx):
        await ctx.send('https://dontasktoask.com/')

    @commands.command()
    async def conventional(self, ctx):
        await ctx.send('https://www.conventionalcommits.org/en/v1.0.0/')

    @commands.command()
    async def nohello(self, ctx):
        await ctx.send('https://nohello.net/')

    @commands.command()
    async def xkcd(self, ctx, arguments = None):
        if not arguments:
            await ctx.send('Please provide arguments e.g g!xkcd <comic_number>')
        else:
            if requests.get('https://xkcd.com/' + arguments + '/info.0.json').status_code == 200:
                xkcd_result = requests.get('https://xkcd.com/' + arguments + '/info.0.json')
                xkcd_result_json = xkcd_result.json()
                xkcd_embed = discord.Embed(
                    title="xkcd: " + xkcd_result_json['safe_title'],
                    url='https://xkcd.com/' + str(arguments) + '/',
                    type='image',
                    description=xkcd_result_json['alt']
                    )
                xkcd_embed.set_image(url=xkcd_result_json['img'])
                xkcd_embed.set_footer(text='xkcd #' + str(arguments))
                await ctx.send(embed=xkcd_embed)


def setup(bot):
    bot.add_cog(Utility(bot))
