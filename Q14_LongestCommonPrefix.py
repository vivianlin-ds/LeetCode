def longestCommonPrefix(self, strs: list[str]) -> str:
    # Need to compare each word in string and return common prefix
    strs.sort(key=len)   # Sort the list by length of word
    oneword = strs[0]    # For one worded strings, len=1
    prefix = ""

    if len(set(strs)) > 1:
        for wordindex in range(0, len(strs[0])):               # Look at individual letters of the word
            current = strs[0][wordindex]                       # Store each letter in current
            for listindex in range(1, len(strs)):              # Look at individual words in string
                if current != strs[listindex][wordindex]:
                    return prefix                              # Exit loop if no common letter
            prefix += current                                  # Add current to prefix only after all are common
        return prefix
    return oneword


def main():
    print(longestCommonPrefix(self=True, strs=["flower", "flow", "flight"]))
    print(longestCommonPrefix(self=True, strs=["dog", "racecar", "car"]))
    print(longestCommonPrefix(self=True, strs=["car", "cir"]))
    print(longestCommonPrefix(self=True, strs=["", ""]))


if __name__ == '__main__':
    main()
