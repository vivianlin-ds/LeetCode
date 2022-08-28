# Question: Given head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    head = ListNode(head)
    prev, curr = None, head

    while curr:
        # Store the current node first.
        temp = curr.next
        # Update the next node to be pointing to the previous node.
        curr.next = prev
        # Set previous node to be the current one to proceed.
        prev = curr
        # Set the current node to the original next node.
        curr = temp

    return prev


# Follow up: Do it recursively.
def recur_reverseList(head):
    head = ListNode(head)

    # Consider the base case
    if not head:
        return None

    # Maintain the new head.
    new_head = head

    # If there is another item in the linked list.
    if head.next:

        new_head = recur_reverseList(head.next)
        # Reverse the link between next node and head
        head.next.next = head
    # Set the next node to null
    head.next = None

    return new_head


def main():
    print(reverseList([1, 2, 3, 4, 5]))
    print(reverseList([1, 2]))
    print(reverseList([]))
    print(recur_reverseList([1, 2, 3, 4, 5]))
    print(recur_reverseList([1, 2]))
    print(recur_reverseList([]))


if __name__ == '__main__':
    main()
    