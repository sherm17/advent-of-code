def get_position_multiplied(file_input):
    horizontal_position = 0
    vertical_position = 0
    aim = 0

    with open(file_input) as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip()
        num = int(line.split()[1])

        if 'up' in line:
            aim -= num
        elif 'down' in line:
            aim += num
        elif 'forward' in line:
            horizontal_position += num
            vertical_position += (aim * num)
    return horizontal_position * vertical_position

position_multipled = get_position_multiplied(file_input='./input')
