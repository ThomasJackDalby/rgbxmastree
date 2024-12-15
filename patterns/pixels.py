from time import sleep
from tools import *

def run2(tree):
    sequence = BY_Z[0]
    for i, id in enumerate(sequence):
        if id == 0:
            tree[id].color = (255, 0, 0)
        else:
            tree[id].color = (255, 255, 255)
        tree[sequence[i-1]].color = (0, 0, 0)

def run(tree):

    colors = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 0, 255),
        (255, 255, 0),
        (0, 255, 255),
    ]
    for z in range(4):
        color = colors[z]
        for i in range(len(BY_Z[z])):
            tree[BY_Z[z][i]].color = color
    
    