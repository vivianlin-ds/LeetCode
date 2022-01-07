# Question: An input parentheses string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def isValid(self, s: str) -> bool:
    # Set up variables so that the corresponding brackets match index numbers
    openbrac = ['(', '{', '[']
    closebrac = [')', '}', ']']

    stack = []

    for brac in s:
        # Add open brackets to stack
        if brac in openbrac:
            stack.append(brac)
        # Evaluate close brackets against last stored open bracket in stack
        elif brac in closebrac:
            # Store the index of the closed bracket to check against last element in stack
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
