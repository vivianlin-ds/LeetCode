# Question: Given in array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and
# nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


def increasingTriple(nums: list[int]) -> bool:
    max1 = float('inf')
    max2 = float('inf')
    for n in nums:
        if n <= max1:
            max1 = n
        elif n <= max2:
            max2 = n
        else:
            return True
    return False


def main():
    print(increasingTriple([1, 2, 3, 4, 5]))
    print(increasingTriple([5, 4, 3, 2, 1]))
    print(increasingTriple([2, 1, 5, 0, 4, 6]))


if __name__ == '__main__':
    main()
