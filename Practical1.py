def custom_tokenize(input_text):
    tokens = []
    current_token = ""

    for char in input_text:
        if char.isalnum() or char == " ":
            current_token += char
        elif current_token:
            tokens.append(current_token)
            current_token = ""

    if current_token:
        tokens.append(current_token)

    return tokens

def tokenize_all_characters(input_text):
    return list(input_text)

if __name__ == "__main__":
    input_text = input("Enter text for tokenization: ")

    word_tokens = custom_tokenize(input_text)
    char_tokens = tokenize_all_characters(input_text)

    print("\nTokenized Words:")
    print(word_tokens)
    print("\nTokenized Characters:")
    print(char_tokens)
