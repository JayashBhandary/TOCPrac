def count_in(inputstr):
    ones,zeros = 0,0

    for char in inputstr:
        if char == '1':
            ones += 1
        elif char == '0':
            zeros += 1
    print(ones)
    print(zeros)

    if(ones == zeros):
        print("String is accepted")
    else:
        print("String is rejected")

inputstr = input("Enter a string with 1s and 0s: ")
count_in(inputstr)
