# Question: Given 0-indexed n x n int matrix grid, return number of pairs (ri, cj) such that row ri and column cj are
# equal. A row and column pair is considered euqal if they contain same elements in the same order.

def equalPairs(grid: list[list[int]]) -> int:
    hash_dict = dict()
    res = 0
    n = len(grid)
    for i in range(n):
        if str(grid[i]) not in hash_dict.keys():
            hash_dict[str(grid[i])] = 1
        else:
            hash_dict[str(grid[i])] += 1

    for i in range(n):
        col = []
        for j in range(n):
            col.append(grid[j][i])
        if str(col) in hash_dict.keys():
            res += hash_dict[str(col)]
    return res


def main():
    print(equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
    print(equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))


if __name__ == '__main__':
    main()
