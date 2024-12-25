import random

COLOURS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
]

class Light:

    def __init__(self, light_id):
        self.light_id = light_id
        self.color = None
        self.delay = 0

    def update(self, tree_value):
        if self.delay > 0:
            self.delay -= 1
        else:
            if self.color is None:
                self.color = random.choice(COLOURS)
                tree_value[self.light_id] = self.color
            else:
                self.color = None
                tree_value[self.light_id] = (0, 0, 0)
            self.delay = random.randint(10, 50)

lights = [Light(id) for id in range(12)]

def run(tree):
    tree_value = list(tree.value)
    for light in lights:
        light.update(tree_value)
    tree.value = tuple(tree_value)
    