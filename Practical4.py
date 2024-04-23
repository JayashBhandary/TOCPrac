def check(in_sequence):
    state = 0
    for digit in in_sequence:
        if state == 0 and digit == '0':
            pass
        elif state == 0 and digit == '1':
            state = 1
        elif state == 1 and digit == '1':
            state = 2
        elif state == 2 and digit == '1':
            return True
        else:
            state = 0

    return False

def main():
    user_input = input("Enter a string our 0s and 1s")
    if check(user_input):
        print("Accepted")
    else:
        print("Rejected")

if __name__ == "__main__":
    main()