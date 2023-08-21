# Question: Given head of a linked list head, in which each node contains an int.
# Between every adjacent nodes, insert new nodes with value equal to the greatest common divisor of them.
# Greatest common divisor: Largest positive int that evenly divides both numbers.
# Return linked list after insertion.
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertGreatestCommonDivisors(head) -> ListNode:
    head = ListNode(head)
    left, right = head, head.next
    while right:
        left_num, right_num = left.val, right.val
        gcd = math.gcd(left_num, right_num)
        new_node = ListNode(gcd)
        left.next = new_node
        new_node.next = right
        left = right
        right = right.next
    return head


def main():
    insertGreatestCommonDivisors([18, 6, 10, 3])


if __name__ == '__main__':
    main()
