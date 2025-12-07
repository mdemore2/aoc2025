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


def slowly_turn_dial(current_pos: int, instruction: str) -> int:
    password_inc = 0
    steps = int(instruction[1:])
    direction = instruction[0]
    remaining_steps = steps
    while remaining_steps > 0:
        if remaining_steps > 99:
            chunk_steps = 99
            remaining_steps -= 99
        else:
            chunk_steps = remaining_steps
            remaining_steps = 0
        if direction == 'L':
            current_pos = current_pos - chunk_steps
            if current_pos <= 0:
                password_inc += 1
            current_pos = current_pos % 100
        else:
            current_pos = current_pos + chunk_steps
            if current_pos > 99:
                password_inc += 1
            current_pos = current_pos % 100

    return password_inc, current_pos


def get_0x_password(input_file: str) -> int:
    password = 0
    current_pos = 50  # starting pos
    with open(input_file, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            password_inc, current_pos = slowly_turn_dial(current_pos, line)
            password += password_inc
    return password
