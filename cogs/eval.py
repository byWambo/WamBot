from discord.ext import commands
from utils import evaluator
from utils import embeds


class Eval:

    def __init__(self, bot):
        self.bot = bot
        self.no = ['import', 'os', 'bot.http.token', 'self.bot.http.token']

    @commands.command(name='eval')
    async def _eval(self, ctx):
        text = ctx.message.content
        try:

            begin = text.find('```py')
            code = text[begin + 6:].rstrip('```')
            if 'import' in code:
                return await ctx.send('YO! YOU BAD BOIIIII!')
            elif 'bot' in code:
                return await ctx.send('Sorry bro, no d.py in Eval')

            response = str(evaluator.eval_py_out(code)[0].decode('utf-8'))

            return await ctx.send(embed=embeds.Eval.get(code, response))

        except Exception as e:
            return await ctx.send(f'An error occured, during this process: **{e}**')
