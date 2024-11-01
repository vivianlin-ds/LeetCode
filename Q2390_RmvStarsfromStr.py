# Question: Given string s, whcih contains stars *. In one operation, choose a star in s, remove closest non-star
# character to its left, as well as remove star itself. Return string after all stars have been removed. Note: Input
# will be generated such that operation is always possible and the resulting string will always be unique.

def removeStars(s: str) -> str:
    res = []
    for c in s:
        if len(res) > 0 and c == "*":
            res.pop()
        else:
            res.append(c)
    return "".join(res)


def main():
    print(removeStars("leet**cod*e"))
    print(removeStars("erase*****"))


if __name__ == '__main__':
    main()
