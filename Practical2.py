import re

def generate_string(n):
    grammar = {
        "S": ["a", "b", "aSb"]
    }

    regex = generate_regex(grammar)
    regex = regex.replace("S", "")

    string = re.sub(r"a", "a" * n, regex)
    string = re.sub(r"b", "b" * n, string)
    return string


def generate_regex(grammar):
    regex = ""
    for non_terminal, production in grammar.items():
        if len(production) == 1:
            regex += production[0]
        else:
            regex += "(" + "|".join(production) + ")"

    return regex

n = int(input("Enter the value of X: "))
string = generate_string(n)
print("output:", string)
