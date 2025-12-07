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
