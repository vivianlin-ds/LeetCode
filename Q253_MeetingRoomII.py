def minMeetingRooms(intervals: list[list[int]]) -> int:
    if intervals == []:
        return 0
    # Sort the intervals
    sorted_int = sorted(intervals, key=lambda x: x[0])

    import heapq
    heap = []
    heapq.heappush(heap, sorted_int[0][1])
    min_room = 1

    for start, end in sorted_int[1:]:
        # If smallest meeting is less than incoming start of meeting, room is reused
        if heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        min_room = max(len(heap), min_room)

    return min_room
        

if __name__ == "__main__":
    i1 = [[0, 30], [5, 10], [15, 20]]
    i2 = [[7, 10], [2, 4]]
    i3 = [[0,10],[1,5],[2,6]]

    print(minMeetingRooms(i1))
    print(minMeetingRooms(i2))
    print(minMeetingRooms(i3))