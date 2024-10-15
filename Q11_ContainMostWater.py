# Question: Given int array height of length n. There are n vertical lines drawn s.t two endpointsr of ith line are
# (i, 0) and (i, height[i]). Find two lines that together with x-axis forma container s.t. container contains most
# water. Return max amount of water a container can store.


def maxArea(height: list[int]) -> int:
    area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        w = right - left
        h = min(height[right], height[left])
        new_area = w * h
        area = max(area, new_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return area


def main():
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(maxArea([1, 1]))


if __name__ == '__main__':
    main()