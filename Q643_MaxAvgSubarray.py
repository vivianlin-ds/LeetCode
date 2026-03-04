# Question: Given int array nums with n elements and integer k. Find contiguous subarray whose length is equal to k
# that has max avg value and return the average.

# def findMaxAverage(nums: list[int], k: int) -> float:
#     window_sum = sum(nums[:k])
#     max_sum = window_sum

#     for i in range(k, len(nums)):
#         window_sum += nums[i] - nums[i - k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum / k

def findMaxAverage(nums: list[int], k: int) -> float:
    left = 0
    max_sum = window_sum = sum(nums[:k])

    for right in range(k, len(nums)):
        print(f"{left} index to {right} index has window {nums[left:right]} and sum to {window_sum} with max {max_sum}")

        max_sum = max(max_sum, window_sum - nums[left] + nums[right])
        window_sum = window_sum - nums[left] + nums[right]
        left += 1
        print(f"window {window_sum} and max {max_sum}")
        
    return max_sum / k 


def main():
    print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
    print(findMaxAverage([5], 1))
    print(findMaxAverage([0, 1, 1, 3, 3], 4))
    print(findMaxAverage([4, 0, 4, 3, 3], 5))


if __name__ == '__main__':
    main()