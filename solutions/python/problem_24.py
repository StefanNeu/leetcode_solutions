from typing import Optional

from _pytest.fixtures import fixture

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        current_node = head
        i = 0
        new_head = head
        while current_node is not None and current_node.next is not None:
            next_node = current_node.next
            current_node.next = next_node.next
            next_node.next = current_node
            if i == 0:
                new_head = next_node
                i += 1
            else:
                pre_node.next = next_node
            pre_node = current_node
            current_node = current_node.next
        return new_head

@fixture()
def sol():
    return Solution()


def test_1(sol: Solution):
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    x = sol.swapPairs(head)
    pass

def test_2(sol: Solution):
    head = None
    x = sol.swapPairs(head)
    pass

def test_3(sol: Solution):
    head = ListNode(1, None)
    x = sol.swapPairs(head)
    pass

