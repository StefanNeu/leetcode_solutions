from collections import deque
from typing import Optional

from _pytest.fixtures import fixture

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        twins = deque()
        current = head
        end = current.next
        while 1:
            twins.append(current.val)
            if end.next is None:
                current = current.next
                break
            current = current.next
            end = end.next.next

        current_max = 0
        while twins:
            current_max = max(current_max, twins.pop() + current.val)
            current = current.next
        return current_max


@fixture()
def sol():
    return Solution()


def test_1(sol: Solution):
    head = ListNode(2, ListNode(4, ListNode(1, ListNode(3, ListNode(7, ListNode(8, None))))))
    assert sol.pairSum(head) == 11

def test_2(sol: Solution):
    head = ListNode(1, ListNode(100000, None))
    assert sol.pairSum(head) == 100001


