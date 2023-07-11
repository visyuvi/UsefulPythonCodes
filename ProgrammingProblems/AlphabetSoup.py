def alphabetSoup(string):
    li = sorted(list(string))
    lowerLi = sorted(list(string.lower()))
    caps = []
    newString = ''

    for char in li:
        if char.isupper():
            caps.append(char)

    for letter in lowerLi:
        if caps.count(letter.upper()) != 0:
            newString += letter.upper()
            caps.remove(letter.upper())
        else:
            newString += letter

    return newString


word = input('Enter a string')
print(alphabetSoup(word))
