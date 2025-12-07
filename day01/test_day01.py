from day01 import turn_dial


def test_turn_dial():
    current_pos = 11
    instruction = 'R8'
    assert turn_dial(current_pos, instruction) == 19


def test_turn_dial_left_edge():
    current_pos = 0
    instruction = 'L1'
    assert turn_dial(current_pos, instruction) == 99


def test_turn_dial_right_edge():
    current_pos = 99
    instruction = 'R1'
    assert turn_dial(current_pos, instruction) == 0
