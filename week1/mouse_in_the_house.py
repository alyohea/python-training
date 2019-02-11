import itertools
import math

MOUSE = '*'
BARRIER = '#'


def init(house):
    with open('house.txt') as f:
        w, h = [int(i) for i in f.readline().split()]
        for i, line in enumerate(f):
            cells = line.split()
            for j, c in enumerate(cells):
                house.append(c)


def surrounding_cells_weights(cells_for_checking, w, h, i, j):
    cells = []
    surrounding_cells_coords = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for new_i, new_j in surrounding_cells_coords:
        if 0 <= new_i < w and 0 <= new_j < h and cells_for_checking[new_i, new_j] >= 0:
            cells.append(cells_for_checking[new_i, new_j])
    return cells if cells else -2


def find_heights(house, weights):
    w, h = len(house), len(house[0])
    i_mouse, j_mouse = [(i, line.find(MOUSE)) for i, line in enumerate(house) if MOUSE in line][0]
    cells_to_check = [(i_mouse, j_mouse)]
    cells = {i: math.inf for i in itertools.product(range(w), range(h))}
    cells[(i_mouse, j_mouse)] = 0
    for i, j in list(cells):
        if house[i][j] == BARRIER:
            cells.update({(i, j): -1})
    for i, j in cells_to_check:
        surrounding_cells_coords = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for new_i, new_j in surrounding_cells_coords:
            if 0 <= new_i < w and 0 <= new_j < h and cells[new_i, new_j] >= 0 and (new_i, new_j) not in cells_to_check:
                cells[new_i, new_j] = min(surrounding_cells_weights(cells, w, h, new_i, new_j)) + 1
                cells_to_check.append((new_i, new_j))
    for c in cells:
        cells[c] = -1 if cells[c] == math.inf else cells[c]
    for i in range(w):
        weights.append(' '.join(list(map(lambda x: str(x), list(cells.values())[i * h:(i + 1) * h]))))


def main():
    weights = []
    house = []
    init(house)
    find_heights(house, weights)
    for w in weights:
        print(w)


if __name__ == '__main__':
    main()
