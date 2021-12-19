with open('input.txt', encoding='utf-8') as f:
    x, y, aim = 0, 0, 0
    for instruction in f.readlines():
        direction, unit = instruction.split()
        unit = int(unit)
        if direction == 'forward':
            x += unit
            y += (aim * unit)
        elif direction == 'down':
            aim += unit
        elif direction == 'up':
            aim -= unit
        else:
            pass

    print(x * y)
