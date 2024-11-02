# Question: Given encoded string, returns its decoded string. Encoding rul,e is k[encoded _string], where the
# encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a
# positive int. Assume input string is always valid, with no extra white sapces, sqaure brakets are well formed etc.
# Also assume that the original data does not contain any digits and that digits are only for those repeated numbers,
# k.

def decodeString(s: str) -> str:
    stack = []
    for c in s:
        if c != "]":
            stack.append(c)

        else:
            print("STACKING", stack)
            current = ""
            while stack[-1] != "[":
                current = stack.pop() + current
            # Remove the [
            stack.pop()

            k = ""
            while stack and stack[-1].isnumeric():
                k = stack.pop() + k
            print(k, current)
            current = int(k) * current
            stack.append(current)

    return "".join(stack)


def main():
    print(decodeString("3[a]2[bc]"))
    print(decodeString("3[a12[c]]"))
    print(decodeString("2[abc]3[cd]ef"))


if __name__ == '__main__':
    main()
