text = input("Enter a text: ")
chars_of_text = list(text)

char_count = {char: text.count(char) for char in text}

print(char_count)
