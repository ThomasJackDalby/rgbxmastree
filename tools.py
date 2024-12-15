# need a funky 3d reference for the lights on the tree

BY_Z = {
    0 : [0, 7, 19, 24, 12, 6, 15, 16],
    1 : [1, 8, 20, 23, 11, 5, 14, 17],
    2 : [2, 9, 21, 22, 10, 4, 13, 18],
    3 : [3]
}
BY_FACE = [[BY_Z[0][i], BY_Z[1][i], BY_Z[2][i]] for i in range(8)]
BY_SIDE = [BY_FACE[2*i] + BY_FACE[2*i + 1] for i in range(4)]