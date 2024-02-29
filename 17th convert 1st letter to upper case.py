def convert_and_join(sentence):
    words = sentence.split()  # Split the sentence into words
    capitalized_words = [word.capitalize() for word in words]  # Capitalize the first letter of each word
    result = '.'.join(capitalized_words)  # Join the words with a period (.)
    return result

# Example usage:
sentence = "this is  a cat"
converted_sentence = convert_and_join(sentence)
print(converted_sentence)
