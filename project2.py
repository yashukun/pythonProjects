alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
import art as lol

print(lol.logo)
direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

display = []
display = list(text)
encrypt_msg = []
decrypt_msg = []


def caesar(text, shift, direction):
    if direction == "encode":
        for i in display:
            if i not in alphabet:
                encrypt_msg.append(i)

            else:
                var = alphabet.index(i)
                new_var = var + shift

                if new_var >= 25:
                    b = alphabet[new_var - 26]
                    encrypt_msg.append(b)

                else:
                    a = alphabet[var + shift]

                    encrypt_msg.append(a)
        print(f"The encrypted message {''.join(encrypt_msg)}")
        encrypt_msg.clear()
        display.clear()
    elif direction == "decode":

        for i in display:
            if i not in alphabet:
                decrypt_msg.append(i)
            else:

                var = alphabet.index(i)

                a = alphabet[var - shift]
                decrypt_msg.append(a)

        print(f"The decrypted message {''.join(decrypt_msg)}")
        decrypt_msg.clear()
        display.clear()

    else:
        print("Invalid choice you can only encode or decode the word")


caesar(text, shift, direction)

gg = input("do you continue? Type 'yes'or'no'.\n")
while gg == "yes":
    direction_2 = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text_2 = input("Type your message:\n").lower()
    display = list(text_2)
    shift_2 = int(input("Type the shift number:\n"))
    caesar(text=text_2, shift=shift_2, direction=direction_2)
    gg = input("do you continue? Type 'yes'or'no'.\n")
print("Good bye")

# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
