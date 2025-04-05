asciiPrintable = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
                  '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<',
                  '=', '>', '?', '@', 'A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                  'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                  'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                  'y', 'z', '{', '|', '}', '~']


def caesarEncrypt(words):
    resultWord = ""
    for char in words:
        for char2 in asciiPrintable:
            if char == char2:
                index = asciiPrintable.index(char2)
                newIndex = index + 3
                if newIndex > len(asciiPrintable):
                    newIndex = newIndex - len(asciiPrintable)
                    resultWord += asciiPrintable[newIndex]
                elif newIndex < 0:
                    newIndex = len(asciiPrintable) + newIndex
                    resultWord += asciiPrintable[newIndex]
                else:
                    resultWord += asciiPrintable[newIndex]
    print(resultWord)


def caesarDecrypt(words):
    resultWord = ""
    for char in words:
        for char2 in asciiPrintable:
            if char == char2:
                index = asciiPrintable.index(char2)
                newIndex = index - 3
                if newIndex > len(asciiPrintable):
                    newIndex = newIndex - len(asciiPrintable)
                    resultWord += asciiPrintable[newIndex]
                elif newIndex < 0:
                    newIndex = len(asciiPrintable) + newIndex
                    resultWord += asciiPrintable[newIndex]
                else:
                    resultWord += asciiPrintable[newIndex]
    print(resultWord)


def vigenereEncrypt(words, password):
    resultWord = ""
    passwordNumbers = []
    lengthOfWords = len(words)
    passwordNumbersForWordLength = []
    finalIndex = 0
    for char in password: 
        for char2 in asciiPrintable:
            if char == char2:
                passwordNumbers.append(asciiPrintable.index(char2))

    while lengthOfWords > 0:
        for item in passwordNumbers:
            passwordNumbersForWordLength.append(item)
            lengthOfWords -= 1
            if lengthOfWords < 1:
                break
        
    for char3 in words:
        for char2 in asciiPrintable:
            if char3 == char2:
                finalIndex = asciiPrintable.index(char2) + passwordNumbersForWordLength[words.index(char3)]
                if finalIndex > len(asciiPrintable):
                    finalIndex = finalIndex - len(asciiPrintable)
                    resultWord += asciiPrintable[finalIndex]
                elif finalIndex < 0:
                    finalIndex = len(asciiPrintable) + finalIndex
                    resultWord += asciiPrintable[finalIndex]
                else:
                    resultWord += asciiPrintable[finalIndex]

    print(resultWord)

def vigenereDecrypt(words, password):
    resultWord = ""
    passwordNumbers = []
    lengthOfWords = len(words)
    passwordNumbersForWordLength = []
    finalIndex = 0
    for char in password: 
        for char2 in asciiPrintable:
            if char == char2:
                passwordNumbers.append(asciiPrintable.index(char2))

    while lengthOfWords > 0:
        for item in passwordNumbers:
            passwordNumbersForWordLength.append(item)
            lengthOfWords -= 1
            if lengthOfWords < 1:
                break
        
    for char3 in words:
        for char2 in asciiPrintable:
            if char3 == char2:
                finalIndex = asciiPrintable.index(char2) - passwordNumbersForWordLength[words.index(char3)]
                if finalIndex > len(asciiPrintable):
                    finalIndex = finalIndex - len(asciiPrintable)
                    resultWord += asciiPrintable[finalIndex]
                elif finalIndex < 0:
                    finalIndex = len(asciiPrintable) + finalIndex
                    resultWord += asciiPrintable[finalIndex]
                else:
                    resultWord += asciiPrintable[finalIndex]

    print(resultWord)
    
caesarEncrypt("alking about the history and current state of death metal and re~")

caesarDecrypt("donlqj#derxw#wkh#klvwru|#dqg#fxuuhqw#vwdwh#ri#ghdwk#phwdo#dqg#uh")

vigenereEncrypt("my brain is melting", "catbus")

vigenereDecrypt("Q[tEhUMPtMitQGaWMPK", "catbus")
