# Question: Given two binary strings a and b, return their sum as binary string

def addBinary(a: str, b: str) -> str:
    # Convert binary strings to integers first
    a = int(a, 2)
    b = int(b, 2)
    # Since bin() gives 0b in front of the binary string by default, read from third letter
    return bin(a+b)[2:]


# Other methods to format binary strings
# print('{0:b}'.format(x))
# print(format(x, 'b'))
# print(f"{x:b}")


def main():
    print(addBinary(a="11", b="1"))
    print(addBinary(a="1010", b="1011"))


if __name__ == '__main__':
    main()