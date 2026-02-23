def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen.keys() and i - seen[nums[i]] <= k:
            return True
        seen[nums[i]] = i
    return False

if __name__ == '__main__':
    n1 = [1,2,3,1]
    k1 = 3
    n2 = [1,0,1,1]
    k2 = 1
    n3 = [1,2,3,1,2,3]
    k3 = 2

    print(containsNearbyDuplicate(nums=n1, k=k1))
    print(containsNearbyDuplicate(nums=n2, k=k2))
    print(containsNearbyDuplicate(nums=n3, k=k3))