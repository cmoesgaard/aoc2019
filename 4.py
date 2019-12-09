import collections
import functools

values = range(137683, 596254)


def is_valid(number, filter_fn):
    stringified = str(number)
    # Check for decreasing values
    if str.join('', sorted(stringified)) != stringified:
        return False

    counter = collections.Counter(stringified)
    if not list(filter(filter_fn, counter.values())):
        return False
    return True


def part_one():
    is_valid_partial = functools.partial(is_valid, filter_fn=lambda x: x >= 2)
    return len(list(filter(is_valid_partial, values)))


def part_two():
    is_valid_partial = functools.partial(is_valid, filter_fn=lambda x: x == 2)
    return len(list(filter(is_valid_partial, values)))


print(part_one())
print(part_two())
