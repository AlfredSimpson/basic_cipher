baseDictionary = 'abcdefghijklmnopqrstuvwxyz'
encryptedPhrase = []
encryptedDict = {}

def easyRead(encryptedPhrase):
    for word in encryptedPhrase:
        for char in word:
            print(char, end='')
        print(end=' ')

def encryptDict():
    print('Let\'s build the encrypted dictionary! ')
    for i in range(len(baseDictionary)):
        newVal = input('What is '+baseDictionary[i]+' represented by in this new cipher? ')
        #the key is the original letter, the newvalue is the encrypted letter
        encryptedDict[baseDictionary[i]] = newVal

def encryptIt():
    print('Encrypting something new.')
    encryptedPhrase.clear()
    oldSentence = input('What do you want to encrypt? ')
    tempBreak = oldSentence.split()
    for word in tempBreak:
        newWord = []
        for char in word:
            if char in baseDictionary:
                newLet = encryptedDict[char]
                newWord.append(newLet)
            else:
                newWord.append(char)
        encryptedPhrase.append(newWord)
    return easyRead(encryptedPhrase)

encryptDict()
encryptIt()
