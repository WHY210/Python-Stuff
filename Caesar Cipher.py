userinput = str(input("Enter your text:"))
shift_value = int(input("Enter your shift Value:"))

text = ""
for alphabet in userinput:
    if not alphabet.isalpha():
        text += alphabet
    else:
        alphabet = alphabet.upper()
        neword = ord(alphabet) + shift_value
        if neword > 90:
            if (neword-90) % 26 == 0:
                neword = 90
            else:
                neword = 64 + (neword-90) % 26
        text += chr(neword)

print(text)