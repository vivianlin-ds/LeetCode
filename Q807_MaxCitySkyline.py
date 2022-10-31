# Question: Given city composed of n x n blocks, where each block contains
# single building shaped like vertical square prism. Given n x n 0-indexed int matrix grid
# where grid[r][c] = Height of the building located in block at row r and column c.
# Allowed to increase height of any number of buildings by any amount,
# but should not affect city's skyline from any direction.
# Return max total sum that height of buildings can be increased by without changing city's skyline.


def maxIncreaseKeepingSkyline(grid: list[list[int]]) -> int:
    # Get the maximum number in each row and column.
    max_row = [max(x) for x in grid]
    max_col = list(map(max, zip(*grid)))
    res = 0

    # Loop through entire matrix to calculate how much can be added.
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Each building cannot exceed the maximum row or maximum column (whichever one is lower).
            limit = min(max_row[i], max_col[j])
            if grid[i][j] < limit:
                res += limit - grid[i][j]
    return res


def main():
    print(maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
    print(maxIncreaseKeepingSkyline([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))


if __name__ == '__main__':
    main()
