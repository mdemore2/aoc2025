def turn_dial(current_pos: int, instruction: str) -> int:
    steps = int(instruction[1:])
    if instruction[0] == 'L':
        new_pos = current_pos - steps
    else:
        new_pos = current_pos + steps

    return new_pos % 100


def get_password(input_file: str) -> int:
    password = 0
    current_pos = 50  # starting pos
    with open(input_file, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            current_pos = turn_dial(current_pos, line)
            if current_pos == 0:
                password += 1
    return password


print(get_password('day01_input.txt'))
