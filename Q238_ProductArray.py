# Question: Given int array nums, return array answer such that anser[i] is equal to product of all the elements of
# nums except nums[i]


def productExceptSelf(nums: list[int]) -> list[int]:
    # res = []
    # for i in range(len(nums)):
    #     product = 1
    #     for j in range(len(nums)):
    #         if i != j:
    #             product *= nums[j]
    #     res.append(product)

    res = [1] * len(nums)
    left = 1
    for i in range(len(nums)):
        res[i] *= left
        left *= nums[i]

    right = 1
    for i in range(len(nums) -1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res


def main():
    print(productExceptSelf([1, 2, 3, 4]))
    print(productExceptSelf([-1, -1, 0, -3, 3]))
    # print(productExceptSelf("a good      example"))


if __name__ == '__main__':
    main()
