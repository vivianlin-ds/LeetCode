# Question: Given integer array nums (sorted in increasing order), remove duplicates in-place
# Relative order of elements should be kept the same
# k elements after removing val and duplicates, return k after placing final result in the first k slots of nums
# Can only modify the input array in-place with O(1) extra memory.

def removeDuplicates(nums: list[int]) -> int:
    i = 0
    while i < len(nums):
        if nums.count(nums[i]) != 1:
            nums.remove(nums[i])
        else:
            i += 1
    return f"{i}, nums = {nums}"


def main():
    print(removeDuplicates(nums=[1, 1, 2]))
    print(removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


if __name__ == '__main__':
    main()