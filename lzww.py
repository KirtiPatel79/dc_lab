def LZW_encode(string):
    # Initialize the dictionary with single characters
    dictionary = {char: i for i, char in enumerate(set(string))}
    # Keep track of the current character sequence being processed
    current_sequence = ""
    # The list to store the encoded characters
    encoded_chars = []
    
    for char in string:
        # Create a new sequence by appending the current character
        new_sequence = current_sequence + char
        # If the new sequence is in the dictionary, update the current sequence
        if new_sequence in dictionary:
            current_sequence = new_sequence
        else:
            # Add the new sequence to the dictionary
            dictionary[new_sequence] = len(dictionary)
            # Output the index of the current sequence
            encoded_chars.append(dictionary[current_sequence])
            # Reset the current sequence to be just the current character
            current_sequence = char
    
    # Output the index of the final sequence, if it exists
    if current_sequence:
        encoded_chars.append(dictionary[current_sequence])
        
    print("Encoded string: ", encoded_chars)
    print("Dictionary table: ", dictionary)

# Example usage
string = input("Enter the string to be encoded: ")
LZW_encode(string)
