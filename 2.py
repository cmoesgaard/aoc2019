from copy import copy

with open('input/2') as f:
    lines = f.read()
    program = lines.split(',')
    program = list(map(int, program))


def add(memory, x_ptr, y_ptr, res_ptr):
    memory[res_ptr] = memory[x_ptr] + memory[y_ptr]
    return True


def mul(memory, x_ptr, y_ptr, res_ptr):
    memory[res_ptr] = memory[x_ptr] * memory[y_ptr]
    return True


def halt(*args):
    return False


OP_TABLE = {
    1: add,
    2: mul,
    99: halt
}


def intcode(program, noun, verb):
    memory = copy(program)

    memory[1] = noun
    memory[2] = verb

    is_running = True
    instruction = 0
    while is_running:
        op = OP_TABLE[memory[instruction]]
        is_running = op(memory, *memory[instruction + 1:instruction + 4])
        instruction += 4
    return memory[0]


def part_one():
    return intcode(program, 12, 2)


def part_two():
    for noun in range(100):
        for verb in range(100):
            res = intcode(program, noun, verb)
            if res == 19690720:
                return 100 * noun + verb


print(part_one())
print(part_two())
