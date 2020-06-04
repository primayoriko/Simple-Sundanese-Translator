from libParser import *
from matcher import *
import os, sys

class Translator:
    def __init__(self, indoDict="../data/indonesia.txt", sundaDict="../data/sunda.txt"):
        self.libparser = LibParser(indo = indoDict, sunda = sundaDict)
        self.text = []
        self.translation = []
        # self.matcher = Matcher()

    def setText(self, text):
        self.text = text.split(" ")
        self.textLength = len(text)
        return self

    def getTranslation(self):
        return " ".join(self.translation)

    def translate(self, type, method=1):
        if(method == 1):
            matcher = KMPMatcher()
        elif(method == 2):
            matcher = BoyerMooreMatcher()
        else: # method == 3
            matcher = RegexMatcher()

        if(type == "sunda-indo"):
            dictionary = self.libparser.vocabSunda
        else: # type == "indo-sunda"
            dictionary = self.libparser.vocabIndo
        
        i, dictLength = 0, len(dictionary)
        while(i < self.textLength):
            if(type == "sunda-indo" and \
                LibParser.isReservedWord(self.text[i], type)):
                self.translation.append(self.text[i])
                i += 1
            else:
                textToValidate, result = "", ""
                j, k, isFound = 0, 0, False
                while(not isFound and j < dictLength):
                    k = dictionary[j].keyLength
                    textToValidate = " ".join(self.text[i : min([i + k, self.textLength])])
                    print(textToValidate +  ' ' + dictionary[j].key + ' ' + str(k))
                    isFound = matcher.setText(dictionary[j].key)\
                                        .setPattern(textToValidate)\
                                        .match()
                    if(isFound):
                        print("ada jir")
                    if(dictionary[j].key == "abu rokok"):
                        print(textToValidate +  ' ' + dictionary[j].key + ' ' + str(k))
                        print(isFound)
                    if(not isFound):
                        j += 1

                if(not isFound):
                    self.translation.append(self.text[i : min([i + k, self.textLength])])
                    i += 1
                else:
                    self.translation.append(dictionary[j].data.split(" "))
                    i += k

        print(self.translation)
        return " ".join(self.translation)

if __name__=='__main__':
    t = Translator()
    a = "nama saya Riyugan"
    t.setText(a).translate("indo-sunda")

