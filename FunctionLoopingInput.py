def inputInt(prompt="Enter an integer: ", min_value=0, max_value=100):
    """
    Call function isInt() to determine if provided value can be parsed into integer
    and finally convert the string into integer
    :param prompt: User string input
    :param min_value: Limit the minimal input value
    :param max_value: Limit the maximum input value
    :return: integer, continue to prompt user input until valid value
    """
    while True:
        user_input = str(input(prompt))
        try:
            if isInt(user_input) and min_value < int(user_input) < max_value:
                return int(user_input)
            else:
                print(f"Value must be between {min_value} and {max_value}.")
                continue
        except ValueError as e:
            print(f"Please make sure entered value is integer due to reason {e}")
            continue

