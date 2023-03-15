alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(direction, text, shift):
    new_text = ''
    for i in text:
        if direction == "encode":
            x = alphabet.index(i) + shift
            if x > len(alphabet) - 1:
                x -= len(alphabet) - 1
                new_text += (alphabet[x])
            else:
                new_text += (alphabet[x])

        elif direction == "decode":
            x = alphabet.index(i) - shift
            new_text += (alphabet[x])
        else:
            print("invalid input")


ceaser(direction, text, shift)
