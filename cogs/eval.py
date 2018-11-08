import io
import textwrap
import traceback
from contextlib import redirect_stdout

from discord.ext import commands


class Eval:
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None

    @staticmethod
    def cleanup_code(code):
        if code.startswith('```') and code.endswith('```'):
            return '\n'.join(code.split('\n')[1:-1])
        else:
            return code.strip('` \n')

    @commands.command(pass_context=True, hidden=True, name='eval')
    @commands.is_owner()
    async def _eval(self, ctx, *, body: str):
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.message.channel,
            'author': ctx.message.author,
            'server': ctx.message.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{str(value)}\n```')
            else:
                try:
                    if self.bot.http.token in ret:
                        ret = ret.replace(self.bot.http.token, '<Censored Token>')
                        self._last_result = ret
                    await ctx.send(f'```py\n{value}{ret}\n```')
                except TypeError:
                    await ctx.send(f'```py\n{value}{ret}\n```')
