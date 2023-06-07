from typing import List
from _pytest.fixtures import fixture


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_bin = bin(a)[2:]
        b_bin = bin(b)[2:]
        c_bin = bin(c)[2:]

        or_array_len = max(len(a_bin), len(b_bin), len(c_bin))
        a_bin = "0" * (or_array_len - len(a_bin)) + a_bin
        b_bin = "0" * (or_array_len - len(b_bin)) + b_bin
        c_bin = "0" * (or_array_len - len(c_bin)) + c_bin

        flips = 0
        for (a, b, c) in zip(a_bin, b_bin, c_bin):
            if c == "0":
                if a == b == "0":
                    flips += 0
                elif a == b == "1":
                    flips += 2
                else:
                    flips += 1
            else:
                if a == b == "0":
                    flips += 1
                else:
                    flips += 0

        return flips

@fixture()
def sol():
    return Solution()


def test_1(sol: Solution):
    a = 5
    b = 2
    c = 8
    assert sol.minFlips(a, b, c) == 4



