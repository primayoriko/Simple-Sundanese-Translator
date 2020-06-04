import os

class Entry:
    def __init__(self, entry):
        entry = entry.split(' = ')
        self.key = entry[0]
        self.data = entry[1]
        self.keyLength = len(entry[0].split(" "))
    
    # @staticmethod
    # def getComparatorKey(this):
    #     return len(this.key)

class LibParser:
    def __init__(self, indo="../data/indonesia.txt", sunda="../data/sunda.txt"):
        if not os.path.isfile(indo) or not os.path.isfile(indo):
            print('File does not exist.')
            exit(1)
        else:
            with open(indo) as i:
                self.vocabIndo = i.read().splitlines()
                self.reservedIndo = []
                temp = []
                for i in self.vocabIndo:
                    temp.append(Entry(i))
                self.vocabIndo = sorted(temp, key = lambda x : x.keyLength, reverse = True)

            with open(sunda) as s:
                self.vocabSunda = s.read().splitlines()
                self.reservedSunda = ["teh"]
                temp = []
                for i in self.vocabSunda:
                    temp.append(Entry(i))
                self.vocabSunda = sorted(temp, key = lambda x : x.keyLength, reverse = True)

    @staticmethod
    def isReservedWord(word, type = "sunda-indo"):
        if(type == "sunda-indo"):
            return True
        else:
            return False

if __name__=='__main__':
    p = LibParser()
    for i in p.vocabIndo:
        print(i.keyLength)
        # print(i.data)
