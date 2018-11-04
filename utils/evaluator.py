import os
import subprocess
import sys


def eval_py_out(code: str):
    """Evaluates Python3 code by simply creating a py file and running it."""
    file = open('eval.py', 'w', encoding='utf-8')

    code_lines = code.splitlines(keepends=True)

    for line in code_lines:
        file.write(line)

    file.close()
    if sys.platform.startswith('win32'):
        cmd = subprocess.Popen('py -3 eval.py', stdout=subprocess.PIPE)
        output = cmd.communicate()
        os.remove('eval.py')
    else:
        output = os.popen('python3 eval.py').readlines()
        os.remove('eval.py')
    return output
