from time import sleep
from tools import *

def run(tree):
    for i in BY_Z[0]:
        if i == 0:
            tree[i].color = (255, 0, 0)
        else:
            tree[i].color = (255, 255, 255)
        tree[(i-1) % 25].color = (0, 0, 0)
        sleep(0.25)