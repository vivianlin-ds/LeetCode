# Question: Given integer array nums and integer val, remove all val in nums in place.
# k elements after removing val and duplicates, return k after placing final result in the first k slots of nums
# Can only modify the input array in-place with O(1) extra memory.

def removeElement(nums: list[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if val in nums:
            nums.remove(val)
        else:
            k += 1
    return f"{k}, nums={nums}"


def main():
    print(removeElement(nums=[3, 2, 2, 3], val=3))
    print(removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))


if __name__ == '__main__':
    main()