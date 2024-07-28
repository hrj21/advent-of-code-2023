from .day_01 import (
    load,
    DEFAULT_DATA,
    solve_q1
)


def test_q1():
    data = load(DEFAULT_DATA)
    assert solve_q1(data) == 55090
