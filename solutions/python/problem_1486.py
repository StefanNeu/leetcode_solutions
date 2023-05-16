from _pytest.fixtures import fixture


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        output = 0
        for elem in nums:
            output = output ^ elem
        return output


@fixture()
def sol():
    return Solution()


def test_1(sol):
    n = 5
    start = 0

    output = 8
    assert sol.xorOperation(n, start) == output
