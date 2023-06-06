from typing import Optional, List

from _pytest.fixtures import fixture


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        return [arr[0] + diff * i for i in range(len(arr))] == arr

@fixture()
def sol():
    return Solution()


def test_1(sol: Solution):
    arr = [9, 3, 7, 5, 1]
    assert sol.canMakeArithmeticProgression(arr) == True



