import random

# every loop it lights up a random pixel to a random color

def run(tree):
    pixel = random.choice(tree)
    pixel.color = random_color()

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)