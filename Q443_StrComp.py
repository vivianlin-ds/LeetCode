# Question: Given array chars, compress it: Start with empty strings. For each group of consecutive repeating
# characters in chars, if group's length is 1, append character to s. Otherwise, append character followed by group's
# length. Compressed string s should not be returned separated but be stored in input character array. Group lengths
# that are 10+ will be split into multiple characters.
# After input array is modified, return new length of array.
# Algorithm must only use constant extra space.


def compress(chars: list[str]) -> int:
    res = 0
    j = 0
    while j < len(chars):
        count = 0
        alphabet = chars[j]

        while j < len(chars) and chars[j] == alphabet:
            j += 1
            count += 1

        # Update the input array
        chars[res] = alphabet
        res += 1

        if count > 1:
            for n in str(count):
                chars[res] = n
                res += 1
    # print(chars)
    return res


def main():
    print(compress(['a', 'a', 'b', 'b', 'c', 'c', 'c']))
    print(compress(['a']))
    print(compress(['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']))


if __name__ == '__main__':
    main()
