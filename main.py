import os
import sys
import asyncio
import random

print(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "rgbxmastree"))
print(sys.path)

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
