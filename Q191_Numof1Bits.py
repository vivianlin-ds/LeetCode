# Question: Return the number of '1' bits from the int being passed into function.

def hammingWeight(n):
    bits = bin(n)
    count = 0
    # Loop through the binary string to look for '1' bits.
    for n in range(len(bits)):
        if bits[n] == '1':
            count += 1
    return count


def main():
    print(hammingWeight(11))
    print(hammingWeight(128))
    print(hammingWeight(4294967293))


if __name__ == '__main__':
    main()
