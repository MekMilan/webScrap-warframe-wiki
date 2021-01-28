import os
import platform

CLS_CMD = 'clear' if platform.system() == 'Linux' else 'cls'

def cls():
    os.system(CLS_CMD)