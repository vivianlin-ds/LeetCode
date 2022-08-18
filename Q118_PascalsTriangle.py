# Question: Given int numRows, return first numRows of Pascal's triangle.

def generate(numRows):
    # Create the array for the result.
    res = [[1]]
    # Add in the designated number of rows.
    for rows in range(1, numRows):
        # Each row starts with 1.
        row = [1]
        # Add in numbers in between by adding numbers from previous row.
        for numbers in range(1, rows):
            row.append(res[rows-1][numbers-1] + res[rows-1][numbers])
        # Each row ends with 1.
        row.append(1)
        res.append(row)
    return res


def main():
    print(generate(1))
    print(generate(5))


if __name__ == '__main__':
    main()
