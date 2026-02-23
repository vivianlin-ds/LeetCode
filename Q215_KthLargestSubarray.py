def findKthLargest(nums: list[int], k: int) -> int:
    # sorted_nums = sorted(nums, reverse=True)
    # return sorted_nums[k-1]
    
    # Solve without sorting: Maxheap
    import heapq
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)

    for i in range(k-1):
        heapq.heappop(heap)

    return -heapq.heappop(heap)


if __name__ == "__main__":
    n1 = [3,2,1,5,6,4]
    k1 = 2
    n2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    print(findKthLargest(n1, k1))
    print(findKthLargest(n2, k2))