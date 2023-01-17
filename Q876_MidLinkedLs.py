# Question: Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    # # Convert a linked list into a list
    # sl_list = []
    # while head:
    #     sl_list.append(head)
    #     head = head.next
    # mid = len(sl_list) // 2
    # return sl_list[mid]

    # Count number of nodes in linked list
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    # Get the node in the middle
    for i in range(count // 2):
        head = head.next
    return head
