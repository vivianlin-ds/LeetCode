def fizzbuzz(n: int) -> list[str]:  # Defined input n as integer and output as list of string
    res = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append('FizzBuzz')
        elif i % 3 == 0:
            res.append('Fizz')
        elif i % 5 == 0:
            res.append('Buzz')
        else:
            res.append(str(i))
    return res


# Define main entrypoint for all codes
def main():
    print(fizzbuzz(3))
    print(fizzbuzz(5))
    print(fizzbuzz(15))


if __name__ == '__main__':  # initialize the code as main program
    main()
