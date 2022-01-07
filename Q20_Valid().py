def isValid(self, s: str) -> bool:
    # Set up variables so that the brackets matches index number
    openbrac = ['(', '{', '[']
    closebrac = [')', '}', ']']
    stack = []

    for brac in s:
        if brac in openbrac:
            stack.append(brac)
        elif brac in closebrac:
            # Store the index of the closed bracket to check against last element stored
            b_index = closebrac.index(brac)
            # Check if the last element in stack matches the closed bracket
            if (len(stack) > 0) and (openbrac[b_index] == stack[-1]):
                # Remove the last element from stack
                stack.pop()
            else:
                return False
    # Valid parentheses should have nothing in stack left
    return len(stack) == 0


def main():
    print(isValid(self=True, s="()"))
    print(isValid(self=True, s="(]"))
    print(isValid(self=True, s="({})]"))


if __name__ == '__main__':
    main()
