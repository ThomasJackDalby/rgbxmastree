import os
import sys
import asyncio
import random
import importlib

SUBMODULE_FOLDER_PATH = os.path.join(os.path.dirname(__file__), "rgbxmastree")
PATTERNS_FOLDER_PATH = os.path.join(os.path.dirname(__file__), "patterns")

sys.path.insert(0, SUBMODULE_FOLDER_PATH)
from tree import RGBXmasTree

for file_path in os.listdir(PATTERNS_FOLDER_PATH):
    print(file_path)
    my_module = importlib.import_module(file_path)

tree = RGBXmasTree()
tree.off()
exit()

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

def main():

    pattern = 
    
    pass

if __name__ == "__main__":
    main()