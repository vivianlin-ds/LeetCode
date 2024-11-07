# Given linked list of size n, where n is even, the ith node of linked list is known as twin of the (n-1-i)th node.
# Twin sum is defined as sum of a node and its twin. Given head of a linked list with even length, return maxximum
# twin sum of the linked list,


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


def pairSum(head):
    slow = head
    fast = head.next.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow.next

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    maxSum = 0
    while prev:
        maxSum = max(maxSum, head.val + prev.val)
        head = head.next
        prev = prev.next

    return maxSum


def main():
    print(pairSum(createLinkedList([5, 4, 2, 1])))
    print(pairSum(createLinkedList([4, 2, 2, 3])))
    print(pairSum(createLinkedList([1, 100000])))


if __name__ == '__main__':
    main()
