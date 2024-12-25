
is_red = False

def run(tree):
    global is_red
    if is_red:
        tree.color = (255, 0, 0)
    else:
        tree.color = (0, 0, 0)
    is_red = not is_red
