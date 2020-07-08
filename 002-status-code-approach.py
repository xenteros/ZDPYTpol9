def get_number_from_user(result_placeholder):
    try:
        x = int(input('Please enter a number: '))
        result_placeholder.append(x)
        return 0
    except ValueError:
        return 1


if __name__ == '__main__':
    number_placeholder = []
    print(number_placeholder)
    result = get_number_from_user(number_placeholder)
    if result == 0:
        print(f"User's choice is {number_placeholder[0]}.")
    else:
        print("Number was illegal.")