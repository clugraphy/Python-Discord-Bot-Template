import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands

if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class htf(commands.Cog, name="htf"):
    def __init__(self, bot):
        self.bot = bot

   
    # Invest vote comands

    @commands.command(name="investvote")
    async def poll(self, context, *args):
        """
        Create a poll where members can vote for coins to invest in.
        """
        poll_title = " ".join(args)
        embed = discord.Embed(
            title="A new month , a new poll ! In what will we invest next?",
            description=f"{poll_title}",
            color=config.success
        )
        embed.set_footer(
            text=f"Invest vote started by : {context.message.author} • Vote your future profit"
        )
        embed_message = await context.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")


    # Mama Omida joke.

    @commands.command(name="mamaomida")
    async def eight_ball(self, context, *args):
        """
        Ask any question to the bot.
        """
        answers = ['Mama Omida zice ca creste UNI', 'Mama Omida zice ca creste BTC','Mama Omida zice ca creste ETH', 'Has mo MKR' ]
        embed = discord.Embed(
            title="**My Answer:**",
            description=f"{answers[random.randint(0, len(answers))]}",
            color=config.success
        )
        embed.set_footer(
            text=f"Question asked by: {context.message.author}"
        )
        await context.send(embed=embed)

    # @commands.command(name="uni")
    # async def uni(self, context):
    #     """
    #     Get the current price of UNI .
    #     """
    #     url = "https://api.coindesk.com/v1/bpi/currentprice/UNI.json"
    #     # Async HTTP request
    #     async with aiohttp.ClientSession() as session:
    #         raw_response = await session.get(url)
    #         response = await raw_response.text()
    #         response = json.loads(response)
    #         embed = discord.Embed(
    #             title=":information_source: Info",
    #             description=f"UNI price is: ${response['bpi']['USD']['rate']}",
    #             color=config.success
    #         )
    #         await context.send(embed=embed)




def setup(bot):
    bot.add_cog(htf(bot))