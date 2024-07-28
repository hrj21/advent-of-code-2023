from .day_01 import (
    load,
    DEFAULT_DATA,
    solve_q1,
    solve_q2,
)


def test_q1():
    data = load(DEFAULT_DATA)
    assert solve_q1(data) == 55090


def test_q2():
    data = load(DEFAULT_DATA)
    assert solve_q2(data) == 54845
