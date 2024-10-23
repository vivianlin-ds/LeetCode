# Question: Given two 0-indexed int array nums1 and nums2, return list answer of size where
# answer[0] is list of all distinct int in nums1 which are not present in nums 2
# answer[1] is list of all distinct int in nums2 which are not present in nums1
# Note that ints in the lists may be returned in any order

def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    nums1 = set(nums1)
    nums2 = set(nums2)
    return [list(nums1.difference(nums2)), list(nums2.difference(nums1))]


def main():
    print(findDifference([1, 2, 3], [2, 4, 6]))
    print(findDifference([1, 2, 3, 3], [1, 1, 2, 2]))


if __name__ == '__main__':
    main()
