# Given head of linked list, delete the middl enode and return the head of the modified linked list. The middle node
# of linked list of size n is [n/2]th node form the start using 0-based indexing, where [x] denotes largest int less
# than or equal to x.


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


def deleteMiddle(head):
    if head is None or head.next is None:
        return None

    slow = head
    fast = head.next.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    slow.next = slow.next.next

    return head


def main():
    print(printLinkedList(deleteMiddle(createLinkedList([1, 3, 4, 7, 1, 2, 6]))))
    print(printLinkedList(deleteMiddle(createLinkedList([1, 2, 3, 4]))))
    print(printLinkedList(deleteMiddle(createLinkedList([2, 1]))))


if __name__ == '__main__':
    main()
