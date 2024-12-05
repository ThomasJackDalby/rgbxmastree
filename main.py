import os
import sys
import asyncio
import random
import importlib

SUBMODULE_FOLDER_PATH = os.path.join(os.path.dirname(__file__), "rgbxmastree")
PATTERNS_FOLDER_PATH = os.path.join(os.path.dirname(__file__), "patterns")

sys.path.insert(0, SUBMODULE_FOLDER_PATH)
from tree import RGBXmasTree

PATTERNS = {}
sys.path.insert(0, PATTERNS_FOLDER_PATH)
for file_name in os.listdir(PATTERNS_FOLDER_PATH):
    file_name_wo_ext = os.path.splitext(file_name)
    pattern = importlib.import_module(file_name_wo_ext)
    PATTERNS[file_name_wo_ext] = pattern

def main():
    tree = RGBXmasTree()
    pattern = PATTERNS["test"]
    while True:
        pattern.run(tree)

if __name__ == "__main__":
    main()