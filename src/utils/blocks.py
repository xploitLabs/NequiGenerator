import time, sys
from . import colors

# --- ANIMATION
def animINFO(s):
    """An function for animate INFO DATA in the console
* s: The text that will be animated"""
    s = f"{colors.BLUE}[{colors.WHITE}INFO{colors.BLUE}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)

def animDONE(s):
    """An function for animate SUCCESS DATA in the console
* s: The text that will be animated"""
    s = f"{colors.GREEN}[{colors.WHITE}DONE{colors.GREEN}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)


def animERROR(s):
    """An function for animate ERROR DATA in the console
* s: The text that will be animated"""
    s = f"{colors.RED}[{colors.WHITE}ERROR{colors.RED}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)

def animDEBUG(s):
    """An function for animate DEBUG DATA in the console
* s: The text that will be animated"""
    s = f"{colors.MAGENTA}[{colors.WHITE}DEBUG{colors.MAGENTA}] {colors.WHITE}{s}"
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)

def anim(s):
    """An function for animate text in the console
* s: The text that will be animated"""
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)
