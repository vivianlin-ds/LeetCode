def longestCommonPrefix(self, strs: list[str]) -> str:
    # Need to compare each letter in string and return it if common
    # Sort the list alphabetically and list will go from short words to long
    strs.sort()
    prefix = ""

    if len(strs) == 0:     # For edge case, nothing in list
        return prefix
    else:
        for wordindex in range(0, len(strs[0])):   # Set i from 0 to length of first word in sorted list
            current = strs[0][wordindex]
            for listindex in range(1, len(strs)-1):
                if current != strs[listindex][wordindex]:
                    return prefix
                else:
                    prefix += current


def main():
    print(longestCommonPrefix(self=True, strs=["flower", "flow", "flight"]))
    print(longestCommonPrefix(self=True, strs=["dog", "racecar", "car"]))
    print(longestCommonPrefix(self=True, strs=[""]))


if __name__ == '__main__':
    main()
