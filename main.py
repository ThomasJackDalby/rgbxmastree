import os
import sys
import asyncio
import random

sys.path.append(os.path.join(os.path.dirname(__file__), "rgbxmastree"))

from tree import RGBXmasTree

tree = RGBXmasTree()

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

try:
    while True:
        pixel = random.choice(tree)
        pixel.color = random_color()
except KeyboardInterrupt:
    tree.close()
