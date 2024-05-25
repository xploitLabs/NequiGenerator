import time, sys
from . import colors

# --- ANIMATION
def animINFO(s, v=3):
    """An function for animate INFO DATA in the console
* s: The text that will be animated"""
    s = f"{colors.BLUE}[{colors.WHITE}INFO{colors.BLUE}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / (50*v))

def animDONE(s, v=3):
    """An function for animate SUCCESS DATA in the console
* s: The text that will be animated"""
    s = f"{colors.GREEN}[{colors.WHITE}DONE{colors.GREEN}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / (50*v))


def animERROR(s, v=3):
    """An function for animate ERROR DATA in the console
* s: The text that will be animated"""
    s = f"{colors.RED}[{colors.WHITE}ERROR{colors.RED}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / (50*v))

def animINPUT(s, v=3):
    """An function for animate DEBUG DATA in the console
* s: The text that will be animated"""
    s = f"{colors.MAGENTA}[{colors.WHITE}INPUT{colors.MAGENTA}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / (50*v))

def anim(s, v=3):
    """An function for animate text in the console
* s: The text that will be animated"""
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / (50*v))

# --- BLOCKS
def INFO(s):
    s = f"{colors.BLUE}[{colors.WHITE}INFO{colors.BLUE}] {colors.WHITE}{s}"
    return s

def DONE(s, v=3):
    s = f"{colors.GREEN}[{colors.WHITE}DONE{colors.GREEN}] {colors.WHITE}{s}"
    return s

def ERROR(s):
    s = f"{colors.RED}[{colors.WHITE}ERROR{colors.RED}] {colors.WHITE}{s}"
    return s

def INPUT(s, v=3):
    s = f"{colors.MAGENTA}[{colors.WHITE}INPUT{colors.MAGENTA}] {colors.WHITE}{s}{colors.YY}"
    return s