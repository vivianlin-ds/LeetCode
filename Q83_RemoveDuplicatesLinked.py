# Question: Given head of a sorted linked list, delete all duplicates such that each element appears only once
# Return sorted linked list
# Given sorted list is guaranteed to be sorted in ascending order

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    # Doesn't need a dummy node since keeping the head of the sorted linked list constant
    head = ListNode(head)
    current = head

    while current:
        while current.next and current.next.val == current.val:
            # While loop check for the existence of next node and if it's the same value as current
            # Skip to the next node if next is a duplicate, go next.next
            current.next = current.next.next
        else:
            current = current.next

    return head


def main():
    print(deleteDuplicates(head=[1, 1, 2]))
    print(deleteDuplicates(head=[1, 1, 2, 3, 3]))


if __name__ == '__main__':
    main()
