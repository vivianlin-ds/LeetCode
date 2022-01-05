def romanToInt(self, s: str) -> int:
    # Make a dictionary for the roman numerals, all letters assigned to number
    romantrans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    final = 0      # Start final answer at 0
    previous = 0   # Need to define previous outside of loop

    # Roman numerals from left to right, large to small aside from special cases like IV

    for n in s:
        current = romantrans[n]
        if previous < current:    # For cases like IV, previous is smaller than current
            final -= previous     # Subtract I (1) from final answer
            final += current - previous     # Add 5-1 = 4 to final answer
        else:
            final += current      # Normal case
        previous = current        # Store current value in previous at the end of each loop
    return final


def main():
    print(romanToInt(self=True, s="III"))
    print(romanToInt(self=True, s="LVIII"))
    print(romanToInt(self=True, s="MCMXCIV"))


if __name__ == '__main__':
    main()
