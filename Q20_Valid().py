def isValid(self, s: str) -> bool:
    # for n in s:
    #     if n == "(":
    #         s = s.replace("(", ")")
    #     elif n == "{":
    #         s = s.replace("{", "}")
    #     elif n == "[":
    #         s = s.replace("[", "]")
    # count1 = s.count(")")
    # count2 = s.count("}")
    # count3 = s.count("]")
    # return count1 % 2 ==0 and count2 % 2 == 0 and count3 %2 == 0:

    openbrac = ['(', '{', '[']
    closebrac = [')', '}', '}']
    stack = []

    for brac in s:
        if brac in openbrac:
            stack.append(brac)
        elif brac in closebrac:
            b_index = closebrac.index(brac)
            if (len(stack) > 0) and (openbrac[b_index] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return False
    return len(stack) == 0


def main():
    # print(isValid(self=True, s="()"))
    print(isValid(self=True, s="({})]"))


if __name__ == '__main__':
    main()
