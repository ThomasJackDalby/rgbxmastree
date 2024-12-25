import random

COLOURS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 0),
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
                self.delay = random.randint(20, 50)
            else:
                self.color = None
                tree_value[self.light_id] = (0, 0, 0)
                self.delay = random.randint(5, 20)

lights = [Light(id) for id in range(25)]

def run(tree):
    tree_value = list(tree.value)
    for light in lights:
        light.update(tree_value)
    tree.value = tuple(tree_value)
    