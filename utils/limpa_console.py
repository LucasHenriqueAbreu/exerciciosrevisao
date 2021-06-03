import os
from sys import platform

def clean():
    clear = lambda: os.system('export TERM=xterm && clear' if platform == 'linux' else 'cls')
    clear()


