import os

class inputParser:
    @staticmethod
    def prefixSeparator(splittedText, specialChar=None):
        if(specialChar is None):
            specialChar = ['.', ',', '!', '?',')', '(', "'", "\"",\
                            '{', '}', '[', ']', '@', '&']
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
        return splittedText
    
    @staticmethod
    def suffixSeparator(splittedText, specialChar=None):
        if(specialChar is None):
            specialChar = ['.', ',', '!', '?',')', '(', "'", "\"",\
                            '{', '}', '[', ']', '@', '&']
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
        return splittedText

class LibParser:
    class Entry:
        def __init__(self, entry):
            entry = entry.split(' = ')
            self.key = entry[0]
            self.data = entry[1]
            self.keyLength = len(entry[0].split(" "))

    def __init__(self, indo="../data/indonesia.txt", sunda="../data/sunda.txt"):
        if not os.path.isfile(indo) or not os.path.isfile(indo):
            print('File does not exist.')
            # exit(1)
        else:
            with open(indo) as i:
                self.vocabIndo = i.read().splitlines()
                self.specialIndo = []
                temp = []
                for i in self.vocabIndo:
                    temp.append(LibParser.Entry(i))
                self.vocabIndo = sorted(temp, key = lambda x : x.keyLength, reverse = True)

            with open(sunda) as s:
                self.vocabSunda = s.read().splitlines()
                self.specialSunda = ["teh"]
                temp = []
                for i in self.vocabSunda:
                    temp.append(LibParser.Entry(i))
                self.vocabSunda = sorted(temp, key = lambda x : x.keyLength, reverse = True)

    # @staticmethod
    def isSpecialWord(self, word, type):
        if(type == "sunda-indo"):
            return word in self.specialSunda
        else: # type == "indo-sunda"
            return word in self.specialIndo

if __name__=='__main__':
    p = LibParser()
    for i in p.vocabIndo:
        print(i.keyLength)
        # print(i.data)

