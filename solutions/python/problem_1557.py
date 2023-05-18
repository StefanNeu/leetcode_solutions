from typing import List
from _pytest.fixtures import fixture


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = set(range(n))
        for edge in edges:
            if edge[1] in nodes:
                nodes.remove(edge[1])
        return list(nodes)

@fixture()
def sol():
    return Solution()


def test_1(sol: Solution):
    n = 6
    edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    assert sol.findSmallestSetOfVertices(n, edges) == [0, 3]



