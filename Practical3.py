def generate_sequence(string, production):
    new_string = " "
    for char in string:
        if char in production:
            new_string += production[char]
        else:
            new_string += char
    return new_string

if __name__ == "__main__":
    production = {
        'S': 'aAb',
        'A': 'aAb'
    } 
    string = 's'

    for i in range(5):
        print(string)
        string = generate_sequence(string, production)

    r = string.replace("A", "")
    print("final output: " + r)