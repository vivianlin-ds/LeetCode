# Question: Given int rowIndex, return the row of the Pascal's triangle.

def getRow(rowIndex):
    prev_row = []
    # Propagate each row until desired row index is reached.
    for rows in range(rowIndex + 1):
        curr_row = []
        # Generate the Pascal's
        for numbers in range(rows + 1):
            if numbers == rows or numbers == 0:
                curr_row.append(1)
            else:
                curr_row.append(prev_row[numbers - 1] + prev_row[numbers])
        prev_row = curr_row
    return curr_row


def main():
    print(getRow(0))
    print(getRow(1))
    print(getRow(3))


if __name__ == '__main__':
    main()
