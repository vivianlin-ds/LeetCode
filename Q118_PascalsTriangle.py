# Question: Given int numRows, return first numRows of Pascal's triangle.

def generate(numRows):
    # Create the array for the result.
    res = []
    # Add in the designated number of rows.
    for rows in range(numRows):
        row = []
        # Add in Pascal's numbers for each row.
        for numbers in range(rows + 1):
            if numbers == rows or numbers == 0:
                row.append(1)
            else:
                row.append(res[rows-1][numbers-1] + res[rows-1][numbers])
        res.append(row)
    return res


def main():
    print(generate(1))
    print(generate(5))


if __name__ == '__main__':
    main()
