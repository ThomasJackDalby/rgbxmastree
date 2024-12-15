import os
import sys
import importlib
import mqtt
import threading

SUBMODULE_FOLDER_PATH = os.path.join(os.path.dirname(__file__), "rgbxmastree")
PATTERNS_FOLDER_PATH = os.path.join(os.path.dirname(__file__), "patterns")

if True:
    sys.path.insert(0, SUBMODULE_FOLDER_PATH)
    from tree import RGBXmasTree
else:
    from mock_tree import RGBXmasTree

# Dynamically load patterns
PATTERNS = {}
sys.path.insert(0, PATTERNS_FOLDER_PATH)
for file_name in os.listdir(PATTERNS_FOLDER_PATH):
    file_name_wo_ext = os.path.splitext(file_name)[0]
    pattern = importlib.import_module(file_name_wo_ext)
    PATTERNS[file_name_wo_ext] = pattern

def mqtt_task():
    client = mqtt.connect()
    client.loop_forever()

def tree_task():
    tree = RGBXmasTree()
    pattern = PATTERNS["pixels"]
    while True:   
        if mqtt.enabled: pattern.run(tree)
        else: tree.color = (0, 0, 0)

def main():
    threading.Thread(target=mqtt_task).start()
    threading.Thread(target=tree_task).start()

if __name__ == "__main__":
    main()