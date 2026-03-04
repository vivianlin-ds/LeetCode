def minSubarray(nums: list[int], p: int) -> int:
    # Finding the smallest subarray to remove that makes remaining divisible by p
    # (total_sum - subarray_sum ) % p == 0, so total_sum % p == subarray_sum % p 
    target = sum(nums) % p

    if target == 0:
        # Array is already divisible
        return 0

    hashmap = {0: -1}
    current_sum = 0
    min_array = len(nums)

    # Prefix sum {remainder: index}
    for i, n in enumerate(nums):
        current_sum = (current_sum + n) % p 
        needed = (current_sum - target) % p
        if needed in hashmap:
            min_array = min(min_array, i - hashmap[needed])
        hashmap[current_sum] = i

    return -1 if min_array == len(nums) else min_array

if __name__ == "__main__":
    n1 = [3,1,4,2]
    p1 = 6
    n2 = [6,3,5,2]
    p2 = 9
    n3 = [1,2,3]
    p3 = 3
    print(minSubarray(n1, p1))
    print(minSubarray(n2, p2))
    print(minSubarray(n3, p3))