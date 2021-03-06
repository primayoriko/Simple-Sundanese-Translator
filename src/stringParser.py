from matcher import *
import os

class inputParser:
    @staticmethod
    def prefixSeparator(splittedText):
        i = 0
        while(i < len(splittedText)):
            temp = splittedText[i]
            wordLength = len(temp)
            j, needSplit = 0, False
            while(j < wordLength and not temp[j].isalpha()):
                j, needSplit = j + 1, True
            if(j < wordLength and needSplit):
                del splittedText[i]
                splittedText.insert(i, temp[0:j])
                splittedText.insert(i + 1, "<=>")
                splittedText.insert(i + 2, temp[j:wordLength])
                i += 3
            else:
                i += 1
        return splittedText
    
    @staticmethod
    def suffixSeparator(splittedText):
        # specialChar = ['.', ',', '!', '?',')', '(', "'", "\"",\
        #                 '{', '}', '[', ']', '@', '&']
        i = 0
        while(i < len(splittedText)):
            temp = splittedText[i]
            wordLength = len(temp)
            j, needSplit = wordLength - 1, False
            while(j >= 0 and not temp[j].isalpha()):
                j, needSplit = j - 1, True
            if(j >= 0 and needSplit):
                del splittedText[i]
                splittedText.insert(i, temp[0:j + 1])
                splittedText.insert(i + 1, "<=>")
                splittedText.insert(i + 2, temp[j + 1:wordLength])
                i += 3
            else:
                i += 1
        return splittedText
    
    @staticmethod
    def decode(text):
        decodedText, i, textLength = "", 0, len(text)
        while(i < textLength):
            decodedText += text[i]
            if i != textLength - 1 and text[i + 1] != "<=>":
                decodedText += " "
                i += 1
            else:
                i += 2
        return decodedText

    @staticmethod
    def deleteEncoding(text):
        return [word for word in text if word != "<=>"]

class LibParser:
    class Entry:
        def __init__(self, entry):
            entry = entry.split(' = ')
            self.key = entry[0]
            self.data = entry[1]
            self.keyLength = len(entry[0].split(" "))

    def __init__(self, indo="../data/indonesia.txt", sunda="../data/sunda.txt",\
                removedWordsSunda = ["teh"], removedWordsIndo = []):
        if not os.path.isfile(indo) or not os.path.isfile(indo):
            print('File does not exist.')
            exit(1)
        else:
            with open(indo) as i:
                self.vocabIndo = i.read().splitlines()
                self.removedWordsIndo = removedWordsIndo
                temp = []
                for i in self.vocabIndo:
                    temp.append(LibParser.Entry(i))
                self.vocabIndo = sorted(temp, key = lambda x : x.keyLength, reverse = True)

            with open(sunda) as s:
                self.vocabSunda = s.read().splitlines()
                self.removedWordsSunda = removedWordsSunda
                temp = []
                for i in self.vocabSunda:
                    temp.append(LibParser.Entry(i))
                self.vocabSunda = sorted(temp, key = lambda x : x.keyLength, reverse = True)

if __name__=='__main__':
    p = LibParser()
    for i in p.vocabIndo:
        print(i.keyLength)

