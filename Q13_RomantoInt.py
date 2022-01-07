# Question: Given a roman numeral, convert it to an integer.

def romanToInt(self, s: str) -> int:
    # Make a dictionary for the roman numerals, all letters assigned to number
    romantrans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Start final answer at 0
    final = 0
    # Need to define previous outside of loop
    previous = 0

    # Roman numerals from left to right, large to small aside from special cases like IV

    for n in s:
        # Set current to the value corresponding to the key
        current = romantrans[n]

        # For cases like IV, previous is smaller than current
        if previous < current:
            # Example: Subtract I (1) from final answer
            final -= previous
            # Example: Add 5-1 = 4 to final answer
            final += current - previous

        # For normal case
        else:
            final += current

        # Store current value in previous at the end of each loop
        previous = current
    return final


def main():
    print(romanToInt(self=True, s="III"))
    print(romanToInt(self=True, s="LVIII"))
    print(romanToInt(self=True, s="MCMXCIV"))


if __name__ == '__main__':
    main()
