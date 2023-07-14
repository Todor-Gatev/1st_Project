# Read user input
secret_list = input().split()

# Logic
for word in secret_list:
    word_in_chars = []
    word_in_chars += word
    num_chars = ""
    letter_chars = []

    for ch in word_in_chars:
        if ch.isdigit():
            num_chars += ch
        else:
            letter_chars += ch

    letter_chars[0], letter_chars[-1] = letter_chars[-1], letter_chars[0]
    deciphered = chr(int(num_chars)) + "".join(letter_chars)
    print(deciphered, end=' ')
# End of Logic
