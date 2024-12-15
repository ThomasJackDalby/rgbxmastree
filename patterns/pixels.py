from time import sleep

def run(tree):
    for i in range(25):
        if i == 0:
            tree[i].color = (255, 0, 0)
        else:
            tree[i].color = (255, 255, 255)
        tree[(i-1) % 25] = (0, 0, 0)
        sleep(0.5)