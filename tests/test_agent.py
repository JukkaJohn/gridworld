from board import Board


def test_move_up():
    state = Board()
    result = state.nxt_position("up")
    assert result == (1, 0)


def test_move_down():
    state = Board((1, 0))
    result = state.nxt_position("down")
    assert result == (2, 0)


def test_move_left():
    state = Board((2, 2))
    result = state.nxt_position("left")
    assert result == (2, 1)


def test_move_right():
    state = Board((2, 1))
    result = state.nxt_position("right")
    assert result == (2, 2)


def test_black_down():
    state = Board((0, 1))
    result = state.nxt_position("down")
    assert result == (0, 1)


def test_black_up():
    state = Board((2, 1))
    result = state.nxt_position("up")
    assert result == (2, 1)


def test_black_right():
    state = Board((1, 0))
    result = state.nxt_position("right")
    assert result == (1, 0)


def test_black_left():
    state = Board((1, 2))
    result = state.nxt_position("left")
    assert result == (1, 2)


def test_reward_right():
    state = Board((0, 2))
    result = state.nxt_position("right")
    assert result == (0, 3)


def test_not_reward_up():
    state = Board((2, 3))
    result = state.nxt_position("up")
    assert result == (1, 3)


def test_not_reward_right():
    state = Board((1, 2))
    result = state.nxt_position("right")
    assert result == (1, 3)


def test_game_over_1():
    state = Board((0, 3))
    return state.nxt_position(None) == (2, 0)


def test_game_over_2():
    state = Board((1, 3))
    return state.nxt_position(None) == (2, 0)


def test_get_reward():
    state = Board((0, 0))
    assert state.give_reward() == 0

    state = Board((1, 3))
    assert state.give_reward() == -1

    state = Board((0, 3))
    assert state.give_reward() == 1
