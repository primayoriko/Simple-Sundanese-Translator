if __name__=='__main__':
    specialChar = ['.', ',', '!', '?',')', '(',\
                    "'", "\"", '{', '}', '[', ']', '@', '&']
    text = "!halo... & nama ...saya bayu!"
    splittedText = text.split(" ")

    i = 0
    while(i < len(splittedText)):
        temp = splittedText[i]
        wordLength = len(temp)
        j, needSplit = 0, False
        while(j < wordLength and temp[j] in specialChar):
            j, needSplit = j + 1, True
        if(j < wordLength and needSplit):
            del splittedText[i]
            splittedText.insert(i, temp[0:j])
            splittedText.insert(i + 1, temp[j:wordLength])
            i += 2
        else:
            i += 1
        # if(wordLength > 1 and temp[0] in specialChar):
        #     del splittedText[i]
        #     splittedText.insert(i, temp[0])
        #     splittedText.insert(i + 1, temp[1:wordLength])
        #     i += 2
        # else:
        #     i += 1

    i = 0
    while(i < len(splittedText)):
        temp = splittedText[i]
        wordLength = len(temp)
        j, needSplit = wordLength - 1, False
        while(j >= 0 and temp[j] in specialChar):
            j, needSplit = j - 1, True
        if(j >= 0 and needSplit):
            del splittedText[i]
            splittedText.insert(i, temp[0:j + 1])
            splittedText.insert(i + 1, temp[j + 1:wordLength])
            i += 2
        else:
            i += 1

    print(splittedText)