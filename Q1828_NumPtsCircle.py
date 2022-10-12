# Question: Given array points where points[i] = [xi, yi] is the coordinates of ith point on 2D plane.
# Multiple points can have same coordinates.
# Given array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with radius of rj.
# For each queries[j], compute number of points inside the jth circle. Points on border of circle are considered inside.
# Return array answer.
import math


def countPoints(points: list[list[int]], queries: list[list[int]]) -> list[int]:
    # Calculate the euclidean distance between points at the center of the circle
    # and see if distance is less than radius.
    answer = []

    for j in range(len(queries)):
        center = [queries[j][0], queries[j][1]]
        radius = queries[j][2]
        count = 0
        for i in range(len(points)):
            distance = math.dist(center, points[i])
            if distance <= radius:
                count += 1
        answer.append(count)
    return answer


def main():
    print(countPoints(points=[[1, 3], [3, 3], [5, 3], [2, 2]],
                      queries=[[2, 3, 1], [4, 3, 1], [1, 1, 2]]))
    print(countPoints(points=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
                      queries=[[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]))


if __name__ == '__main__':
    main()
