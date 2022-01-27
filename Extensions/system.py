import json
import os
import discord.ext.commands
from discord.ext import commands
from gamedata.scripts.users import User
from gamedata.configs.items.associate_type import associate
from gamedata.scripts.item import get_info_for_tpl


class SystemCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["пинг"])
    async def ping(self, ctx):
        print(type(ctx))
        ping = self.bot.latency
        ping = round(ping * 1000)
        await ctx.send(f"my ping is {ping}ms")

    @commands.command()
    async def descr(self, ctx: discord.ext.commands.context.Context, *args):
        user = User(ctx.author.id)
        if len(args) < 1:
            return
        n = int(args[0])
        if n > len(user.json["inventory"]):
            return
        n -= 1
        if "-j" in args:
            await ctx.send(user.json["inventory"][n])
            return
        data = get_info_for_tpl(user.json["inventory"][n]["tpl"])
        await ctx.send(f'{data["name"]}\n{data["description"]}')
    @commands.command()
    async def inv(self, ctx: discord.ext.commands.context.Context, *args):
        user = User(ctx.author.id)
        if len(ctx.message.mentions):
            user = User(ctx.message.mentions[0].id)
        if "-j" in args:
            await ctx.send(user.json["inventory"])
            return
        if len(args) == 0:
            text = ""
            for i, item in enumerate(user.json["inventory"]):
                item_d = get_info_for_tpl(item["tpl"])
                print(item_d)
                text += f'{i+1}: {item_d["name"]}\n'

            await ctx.send(text)



    @commands.command()
    async def stats(self, ctx: discord.ext.commands.context.Context, *args):
        user = User(ctx.author.id)
        if len(ctx.message.mentions):
            user = User(ctx.message.mentions[0].id)
        if "-j" in args:
            await ctx.send(user.json)
            return
        await ctx.send(f"""id: {user["info"]["id"]}\nhealth: {user["health"]["current"]}/{user["health"]["maximum"]}""")

    @commands.command()
    async def new(self, ctx: discord.ext.commands.context.Context):
        new_user_json = json.load(open(str(os.getcwd()) + f"\\server\\profile_mask.json"))
        new_user_json["info"]["id"] = ctx.author.id
        new_user_json["info"]["nickname"] = ctx.author.nick
        json.dump(new_user_json, open(str(os.getcwd()) + f"\\server\\profiles\\{ctx.author.id}.json", "w"))
        await ctx.send(new_user_json)


def setup(bot):
    bot.add_cog(SystemCog(bot))
