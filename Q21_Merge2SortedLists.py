# Question:  Given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Need to define ListNode as a class since LeetCode question referred to the object type
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    # Make sure everything ran as ListNode
    list1 = ListNode(list1)
    list2 = ListNode(list2)

    # Create dummy node as placeholder
    dummy = ListNode(0)

    # Current pointer in the linked list
    current = dummy

    # Empty list cases
    if list1 == None:
        current.next = list2
        return dummy.next
    elif list2 == None:
        current.next = list1
        return dummy.next

    # Making the merged list
    while list1 and list2:
        if list1.val <= list2.val:
            # Add the number in list1
            current.next = list1
            # Move list1 point to next node
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        # Moves the current pointer to next node
        current = current.next

    # Add any leftover nodes from list
    current.next = list1 or list2

    # Dummy is placeholder, so return next to get the actual nodes
    return dummy.next


def main():
    print(mergeTwoLists(self=True, list1=[], list2=[1, 3, 4]))


if __name__ == '__main__':
    main()
