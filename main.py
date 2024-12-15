import os
import sys
import importlib
import mqtt
import threading
from time import sleep

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
    if file_name.startswith("__"): continue
    file_name_wo_ext = os.path.splitext(file_name)[0]
    pattern = importlib.import_module(file_name_wo_ext)
    PATTERNS[file_name_wo_ext] = pattern

print(PATTERNS)

def mqtt_task():
    client = mqtt.connect()
    client.loop_forever()

def tree_task():
    tree = RGBXmasTree()
    current_pattern = None
    while True:   
        if mqtt.CURRENT_PATTERN is not None:
            if current_pattern != mqtt.CURRENT_PATTERN:
                pattern = PATTERNS[mqtt.CURRENT_PATTERN]
                current_pattern = mqtt.CURRENT_PATTERN
            pattern.run(tree)
        else:
            tree.off()
            sleep(1)

def main():
    for pattern in PATTERNS:
        mqtt.register_component(pattern)

    threading.Thread(target=mqtt_task).start()
    threading.Thread(target=tree_task).start()

if __name__ == "__main__":
    main()