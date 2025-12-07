from day01 import turn_dial, get_password, get_0x_password


def test_turn_dial():
    current_pos = 11
    instruction = 'R8'
    current_pos = turn_dial(current_pos, instruction)
    assert current_pos == 19
    instruction = 'L19'
    current_pos = turn_dial(current_pos, instruction)
    assert current_pos == 0


def test_turn_dial_left_edge():
    current_pos = 0
    instruction = 'L1'
    assert turn_dial(current_pos, instruction) == 99


def test_turn_dial_right_edge():
    current_pos = 99
    instruction = 'R1'
    assert turn_dial(current_pos, instruction) == 0


def test_get_password():
    assert get_password('day01_test_input.txt') == 3


def test_get_0x_password():
    assert get_0x_password('day01_test_input.txt') == 6
