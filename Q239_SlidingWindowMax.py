def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    # Use a queue to store the elements of the current window
    from collections import deque
    queue = deque()
    res = []
    for i in range(len(nums)):
        print(f"Processing index {i}, number {nums[i]}, window size {i-k+1} to {i}")
        print(f"Current queue: {queue}, current result: {res}")

        # Maintain queue to match window size
        while queue and queue[0] < i - k + 1:
            print(f">>Removing index {queue[0]} from queue because it's out of the current window")
            queue.popleft()

        # Keep largest element at front of queue
        while queue and nums[queue[-1]] <= nums[i]:
            print(f"Removing index {queue[-1]} from queue because {nums[queue[-1]]} <= {nums[i]}")
            queue.pop()

        # Add index into the queue
        queue.append(i)
        print(f"Added index {i} to queue, current queue: {queue}")

        if i >= k - 1:
            res.append(nums[queue[0]])
            print(f"Window has reached size {k}, adding max {nums[queue[0]]} to result")
    
    return res

if __name__ == "__main__":
    n1 = [1,3,-1,-3,5,3,6,7]
    k1 = 3

    n2 = [1, -1]
    k2 = 1

    # print(maxSlidingWindow(n1, k1))
    print(maxSlidingWindow(n2, k2))
