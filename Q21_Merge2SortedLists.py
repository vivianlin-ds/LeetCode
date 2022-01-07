# Need to define ListNode as a class since LeetCode question referred to the object type
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Use dummy node to store
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
    else:
        if list1.val <= list2.val:
            # Add the number in list1 to current
            current.next = list1
            # Move list1 point to next node
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        # Add any leftover nodes in list after above if else statements
        current.next = list1 or list2
    return dummy.next


def main():
    print(mergeTwoLists(list1=[1, 2, 4], list2=[1, 3, 4]))


if __name__ == '__main__':
    main()
