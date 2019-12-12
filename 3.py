with open('input/3') as f:
    lines = f.readlines()

paths = [line.split(',') for line in lines]


def make_vectors(path_list):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    vectors = []

    for path in path_list:
        direction = path[0]
        distance = int(path[1:])
        if direction is 'U':
            y2 += distance
        elif direction is 'D':
            y2 -= distance
        elif direction is 'R':
            x2 += distance
        elif direction is 'L':
            x2 -= distance

        vectors.append((x1, y1, x2, y2))

        x1, y1 = x2, y2

    return vectors


def find_intersections(list_a, list_b):





def part_one():
    wire_one = make_vectors(paths[0])
    wire_two = make_vectors(paths[1])

    find_intersections(wire_one, wire_two)
    pass


def part_two():
    pass


print(part_one())
print(part_two())
