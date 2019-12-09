with open('input/6') as f:
    lines = f.readlines()

split = [line.strip().split(')') for line in lines]
orbit_map = {planet: parent for parent, planet in split}


def count_orbits(planet):
    orbits = 0
    parent = orbit_map.get(planet)
    while parent:
        orbits += 1
        parent = orbit_map.get(parent)
    return orbits


def get_orbit_path(planet):
    path = []
    parent = orbit_map.get(planet)
    while parent:
        path.append(parent)
        parent = orbit_map.get(parent)
    return path


def part_one():
    orbit_counts = [count_orbits(planet) for planet in orbit_map]
    return sum(orbit_counts)


def part_two():
    you_path = set(get_orbit_path('YOU'))
    san_path = set(get_orbit_path('SAN'))

    difference = you_path ^ san_path
    return len(difference)


print(part_one())
print(part_two())
