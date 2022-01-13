import discord
from discord.ext import commands

import requests


class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, arguments=None):
        if not arguments:
            await ctx.send('Please provide arguments, syntax: g!userinfo <user>')
        else:
            if requests.get('https://api.github.com/users/' + arguments).status_code == 200:
                userinfo_result = requests.get('https://api.github.com/users/' + arguments)
                userinfo_result_json = userinfo_result.json()
                userinfo_embed = discord.Embed(
                    title=userinfo_result_json['login'],
                    url=userinfo_result_json['html_url']
                )
                userinfo_embed.set_thumbnail(url=userinfo_result_json['avatar_url'])
                userinfo_embed.add_field(name="Name", value=userinfo_result_json['name'], inline=True)
                userinfo_embed.add_field(name="Company", value=userinfo_result_json['company'], inline=True)
                userinfo_embed.add_field(name="Location", value=userinfo_result_json['location'], inline=True)
                userinfo_embed.add_field(name="Public Repos", value=userinfo_result_json['public_repos'], inline=True)
                userinfo_embed.add_field(name="Followers", value=userinfo_result_json['followers'], inline=True)
                userinfo_embed.add_field(name="Following", value=userinfo_result_json['following'], inline=True)
                await ctx.send(embed=userinfo_embed)


def setup(bot):
    bot.add_cog(User(bot))
