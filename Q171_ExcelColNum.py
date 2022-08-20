# Question: Given string columnTitle, which represents column title as appears in an Excel sheet,
# return the corresponding column number.

def titleToNumber(columnTitle):
    offset_ASCII = 64
    letter = 26
    value = 0
    # Need to start off at the end of the string, so reverse the string.
    reversed_col = columnTitle[::-1]
    for i in range(len(columnTitle)):
        # By ASCII standards, A is 65, but for columns, A is 1. Columns are base 26.
        value += (ord(reversed_col[i]) - offset_ASCII) * (letter ** i)
    return value


def main():
    print(titleToNumber("A"))
    print(titleToNumber("AB"))
    print(titleToNumber("ZY"))


if __name__ == '__main__':
    main()
