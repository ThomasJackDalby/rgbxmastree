from time import sleep
from tools import *

def run(tree):
    sequence = BY_Z[0]
    for i, id in enumerate(sequence):
        if id == 0:
            tree[id].color = (255, 0, 0)
        else:
            tree[id].color = (255, 255, 255)
        tree[sequence[i-1]].color = (0, 0, 0)
        sleep(0.25)