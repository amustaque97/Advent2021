with open('input.txt', encoding='utf-8') as f:
    x, y = 0, 0
    for instruction in f.readlines():
        direction, unit = instruction.split()
        unit = int(unit)
        if direction == 'forward':
            x += unit
        elif direction == 'down':
            y += unit
        elif direction == 'up':
            y -= unit
        else:
            pass

    print(x * y)
