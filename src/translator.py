from parser import *
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
            dictionary = self.libparser.vocabIndo
        else: # type == "indo-sunda"
            dictionary = self.libparser.vocabSunda
        
        i, dictLength = 0, len(dictionary)
        while(i < self.textLength):
            if(type == "sunda-indo" and \
                LibParser.isReservedWord(self.text[i], type)):
                self.translation.append(self.text[i])
                i += 1
            else:
                j, k, textToValidate, result = 0, 0, "", ""
                isFound = False
                while(not isFound and j < dictLength):
                    k = len(dictionary[j].key)
                    textToValidate = " ".join(self.text[i : i + k])
                    isFound =  matcher.setText(textToValidate)\
                                        .setPattern(dictionary[j].key)\
                                        .solver()
                    if(not isFound):
                        j += 1

                if(not isFound):
                    self.translation.append(textToValidate.split(" "))
                    i += 1
                else:
                    self.translation.append(dictionary[j].data.split(" "))
                    i += k
        return " ".join(self.translation)

if __name__=='__main__':
    t = Translator()
    a = str(input())
    t.setText(a).translate("indo-sunda")

