# Morse Code Dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.',
    ')': '-.--.-', '@': '.--.-.', '+': '.-.-.',
    '=': '-...-', '_': '..--.-', '"': '.-..-.',
    "'": '.----.', ':': '---...', '[': '-.--.',
    ']': '-.--.-', '!': '-.-.--', ' ': ' ',
}

programme_is_on = True
while programme_is_on:
    # Input Statement
    code = input("What phrase would you like to translate to Morse Code? Type 'exit' to exit.").upper()

    cipher = ''

    if code == "EXIT":
        programme_is_on = False

    else:
        # For loop to replace each character in a string with a value from the dictionary
        for letter in code:
            # Replaces each character in a string with a value form dictionary and adds an empty space after each letter
            cipher += morse_code_dict[letter] + ' '
        print(cipher)

    if code != "EXIT":
        another_go = input("Whould you like to encode/decode another sentence? Type yes or no: ").lower()
        if another_go == "yes":
            programme_is_on = True
        elif another_go == "no":
            programme_is_on = False
        else:
            another_go = input("Would you like to encode/decode another sentence? Type yes or no: ").lower()
