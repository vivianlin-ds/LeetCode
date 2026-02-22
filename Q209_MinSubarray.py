def minSubArrayLen(target: int, nums: list[int]) -> int:
    left = 0
    current_sum = 0
    count = float('inf')

    for i in range(len(nums)):
        current_sum += nums[i]

        while current_sum >= target:
            count = min(count, i - left + 1)
            current_sum -= nums[left]
            left += 1
        
    return count if count != float('inf') else 0

if __name__ == "__main__":
    t1 = 7
    n1 = [2,3,1,2,4,3]

    t2 = 4
    n2 = [1,4,4]

    t3 = 11
    n3 = [1,1,1,1,1,1,1,1]

    t4 = 213
    n4 = [12,28,83,4,25,26,25,2,25,25,25,12]

    print(minSubArrayLen(t1, n1))
    print(minSubArrayLen(t2, n2))
    print(minSubArrayLen(t3, n3))
    print(minSubArrayLen(t4, n4))
