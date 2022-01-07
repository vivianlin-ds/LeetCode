# Question: Find the longest common prefix string amongst an array of strings,
# return empty "" if no common prefix.
def longestCommonPrefix(self, strs: list[str]) -> str:
    # Need to compare each letter of each word in string: strs[a][b]
    # Sort the list by length of word, from shortest to longest word
    strs.sort(key=len)

    # For one worded strings, len=1
    oneword = strs[0]
    # Store extracted letters
    prefix = ""

    if len(strs) > 1:
        # Look at individual letters of the word: b of strs[a][b]
        for wordindex in range(0, len(strs[0])):
            # Store each letter in current
            current = strs[0][wordindex]

            # Look at individual words in string: a of strs[a][b]
            for listindex in range(1, len(strs)):
                # Exit loop if no common letter
                if current != strs[listindex][wordindex]:
                    return prefix

            # Add current to prefix only after loop through all words in list
            prefix += current
        return prefix

    # Return answer for one worded strings
    return oneword


def commonprefix(self, strs: list[str]) -> str:
    # Use zip() instead of multiple loops
    # Give individual letters up to the shortest word
    zip_strs = list(zip(*strs))
    zip_prefix = ""
    for char in zip_strs:
        # Look at individual tuple, use 'set' so no duplication allowed, len == 1 if common
        if len(set(char)) == 1:
            zip_prefix += char[0]
        # End loop if no common letter is found, do not continue past first different letter
        else:
            break
    return zip_prefix


def main():
    print(longestCommonPrefix(self=True, strs=["flower", "flow", "flight"]))
    print(longestCommonPrefix(self=True, strs=["dog", "racecar", "car"]))
    print(longestCommonPrefix(self=True, strs=["car", "cir"]))
    print(longestCommonPrefix(self=True, strs=["", ""]))
    print(commonprefix(self=True, strs=["flower", "flow", "flight"]))
    print(commonprefix(self=True, strs=["dog", "racecar", "car"]))
    print(commonprefix(self=True, strs=["car", "cir"]))
    print(commonprefix(self=True, strs=["", ""]))


if __name__ == '__main__':
    main()
