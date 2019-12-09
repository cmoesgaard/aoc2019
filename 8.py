import collections

with open('input/8') as f:
    digits = f.read().strip()

layers = [digits[i:i + 150] for i in range(0, len(digits), 150)]


def part_one():
    counted_layers = [collections.Counter(layer) for layer in layers]
    sorted_layers = sorted(counted_layers, key=lambda x: x['0'])
    return sorted_layers[0]['1'] * sorted_layers[0]['2']


def part_two():
    pixel_layers = [str.join('', layer) for layer in zip(*layers)]
    pixels = [pixel.replace('2', '')[0] for pixel in pixel_layers]

    lines = [str.join('', pixels[i:i + 25]) for i in range(0, len(pixels), 25)]
    image = str.join('\n', lines).replace('0', '▁').replace('1', '█')

    return image


print(part_one())
print(part_two())
