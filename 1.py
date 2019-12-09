import math

with open('input/1') as f:
    numbers = [int(line) for line in f.readlines()]


def calculate_fuel(number):
    return math.floor(number / 3) - 2


def calculate_total_fuel(number):
    total_fuel = 0
    fuel = calculate_fuel(number)
    while fuel > 0:
        total_fuel += fuel
        fuel = calculate_fuel(fuel)
    return total_fuel


def part_one():
    return sum([calculate_fuel(number) for number in numbers])


def part_two():
    return sum([calculate_total_fuel(number) for number in numbers])


print(part_one())
print(part_two())
