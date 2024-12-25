import math
import colorsys
from tools import BY_Z

SPEED_FACTOR = 0.0001
OFFSET = 0.5

t = 0

def run(tree):
    global t
    t += 1

    for z in BY_Z:
        hue = math.sin(SPEED_FACTOR * t + z * OFFSET)

        tree_value = list(tree.value)
        for i in range(len(BY_Z[z])):
            r, g, b = tree_value[BY_Z[z][i]]
            h, s, v = colorsys.rgb_to_hsv(r, g, b)
            h += hue
            tree_value[BY_Z[z][i]] = hsv2rgb(h, s, v)
        tree.value = tuple(tree_value)

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))