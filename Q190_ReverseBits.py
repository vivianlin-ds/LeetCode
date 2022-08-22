# Question: Given 32 bits unsigned int, return the reverse bits.

def reverseBits(n):
    # Convert the number into binary and get rid of the '0b' prefix
    bits = bin(n)[2:]
    # Add in zeros to make it 32 bits, then reverse it.
    bits = bits.zfill(32)[::-1]
    # Convert binary back into int to avoid ValueError.
    return int(bits, 2)


def main():
    print(reverseBits(43261596))
    print(reverseBits(4294967293))


if __name__ == '__main__':
    main()
