# Question: Given Palindrome string of lowercase, replace exactly one character
# so that the resulting string is not a palindrome and it's lexicographically smallest one possible.
# Return resulting string and if there's no way to replace, return empty string.

def breakPalindrome(palindrome: str) -> str:
    # For any string of one character, there's no way to replace.
    if len(palindrome) == 1:
        return ""

    # Loop through Palindrome until the middle character.
    for n in range(len(palindrome) // 2):
        # Change anything that's no an 'a' to an 'a'.
        if palindrome[n] != "a":
            return palindrome[:n] + "a" + palindrome[n+1:]

    # If everything is already an 'a', make the last character 'b'.
    return palindrome[:-1] + "b"


if __name__ == '__main__':
    print(breakPalindrome("abccba"))
    print(breakPalindrome("a"))
    print(breakPalindrome("ab"))
