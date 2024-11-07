# Given head of linked list, group all nodes with nodd indices together followed by nodes with even indices and
# return the reordered list. First node is considered off and second node is even. Note that relative order inside
# both even and odd groups should remain as it was in the input. Must solve probelm in O(1) extra space complexity
# and O(n) time complexity.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def printLinkedList(head):
    current = head
    res = []
    while current:
        res.append(current.val)
        current = current.next
    return res


def oddEvenList(head):
    if head is None:
        return None

    odd = head
    even_head = even = head.next

    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next

        even.next = even.next.next
        even = even.next

    odd.next = even_head

    return head


def main():
    print(printLinkedList(oddEvenList(createLinkedList([1, 2, 3, 4, 5]))))
    print(printLinkedList(oddEvenList(createLinkedList([2, 1, 3, 5, 6, 4, 7]))))


if __name__ == '__main__':
    main()
