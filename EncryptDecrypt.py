

def caesar(words):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    resultWord = ""
    for char in words:
        for char2 in alphabet:
            if char == char2:
                index = alphabet.index(char2)
                resultWord += alphabet[index + 3]
    print(resultWord)

caesar("dogz")
