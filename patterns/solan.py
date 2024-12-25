from tools import BY_SIDE
from time import sleep

RED = (255, 0, 0)
GREEN = (0, 255, 0)
red = True
index = 0

def run(tree):
    global red
    global index
    color = RED if red else GREEN
    red = not red

    tree_value = list(tree.value)
    for i in range(len(BY_SIDE[index])):
        tree_value[BY_SIDE[index][i]] = color
    tree.value = tuple(tree_value)

    index = (index + 1) % len(BY_SIDE)
    sleep(0.5)
    