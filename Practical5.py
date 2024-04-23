def accept_string_ending_with_101(input_string):
    state=0
    for char in input_string:
        if state == 0 and char == '0':
            pass
        elif state == 0 and char == '1':
            state=1
        elif state == 1 and char == '0':
            state=2
        elif state == 2 and char == '1':
            state=3
        else:
            state=0
    return state


def check():
    user_input = input("Enter a string over 0s and 1s")
    if(accept_string_ending_with_101(user_input)):
        print("Accepted")
    else:
        print("Rejected")


if __name__ == "__main__":
    check()