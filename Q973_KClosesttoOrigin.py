def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    import math
    def distance(x, y):
        return (math.sqrt(x **2 + y ** 2))

    import heapq
    # Store (distance, point) in heap
    heap = []
    res = []
    for p in points:
        dist = distance(p[0], p[1])
        heapq.heappush(heap, (dist, p))
    
    for _ in range(k):
        res.append(heapq.heappop(heap)[1])

    return res

if __name__ == "__main__":
    p1 = [[1,3],[-2,2]]
    k1 = 1
    
    p2 = [[3,3],[5,-1],[-2,4]]
    k2 = 2
    
    print(kClosest(p1, k1))
    print(kClosest(p2, k2))
