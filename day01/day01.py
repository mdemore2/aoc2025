def turn_dial(current_pos: int, instruction: str) -> int:
    steps = int(instruction[1:])
    if instruction[0] == 'L':
        new_pos = current_pos - steps
    else:
        new_pos = current_pos + steps

    if new_pos < 0:
        new_pos = 100 + new_pos  # double negative
    elif new_pos > 99:
        new_pos = new_pos - 100

    return new_pos


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
