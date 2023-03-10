def encode_lz78(text):
    dictionary = {}
    encoded = []
    currentWord = ""
    for c in text:
        newWord = currentWord + c
        if newWord in dictionary:
            currentWord = newWord
        else:
            encoded.append((dictionary.get(currentWord, 0), c))
            dictionary[newWord] = len(dictionary) + 1
            currentWord = ""
    if currentWord:
        encoded.append((dictionary.get(currentWord, 0), None))
    return encoded

def decode_lz78(encoded):
    dictionary = {}
    decoded = []
    currentWord = ""
    for (i, c) in encoded:
        if i == 0:
            decoded.append(currentWord + c)
            dictionary[len(dictionary) + 1] = currentWord + c
            currentWord = ""
        else:
            currentWord = dictionary[i]
            if c is not None:
                decoded.append(currentWord + c)
                dictionary[len(dictionary) + 1] = currentWord + c
                currentWord = ""
    return "".join(decoded)

print("LZ78 Compression and Decompression")
#print("200303108034 | Kirti Patel")
stringToEncode = input("Enter the string you want to compress:")

encoded = encode_lz78(stringToEncode)

print("Encoded string: ", encoded)

decoded = decode_lz78(encoded)
print("Decoded string:", decoded)
