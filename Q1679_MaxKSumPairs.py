# Question: Given int array nums and int k. In one operation, pick two numbers from array whose sum euqals k and
# remove them from the array. Return max number of operations you can perform on the array.


def maxOperations(nums: list[int], k: int) -> int:
    res = 0
    left = 0
    right = len(nums) - 1

    nums.sort()

    while left < right:
        if nums[left] + nums[right] == k:
            res += 1
            left += 1
            right -= 1
        elif nums[left] + nums[right] > k:
            right -= 1
        else:
            left += 1

    return res


def main():
    print(maxOperations([1, 2, 3, 4], 5))
    print(maxOperations([3, 1, 3, 4, 3], 6))


if __name__ == '__main__':
    main()