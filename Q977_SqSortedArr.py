# Question: Given an int array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.


def sortedSquares(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return sorted(nums)


def main():
    print(sortedSquares(nums=[-4, -1, 0, 3, 10]))
    print(sortedSquares(nums=[-7, -3, 2, 3, 11]))


if __name__ == '__main__':
    main()
