def encode(text):
    alphabet = [chr(i) for i in range(256)]
    encoded_text = []
    for char in text:
        index = alphabet.index(char)
        encoded_text.append(index)
        alphabet.pop(index)
        alphabet.insert(0, char)
    return encoded_text

def decode(encoded_text):
    alphabet = [chr(i) for i in range(256)]
    decoded_text = ""
    for index in encoded_text:
        char = alphabet[index]
        decoded_text += char
        alphabet.pop(index)
        alphabet.insert(0, char)
    return decoded_text

text = input("Enter the text to encode: ")
encoded_text = encode(text)
print("Encoded text:", encoded_text)
decoded_text = decode(encoded_text)
print("Decoded text:", decoded_text)
