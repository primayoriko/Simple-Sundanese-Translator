from stringParser import *
from matcher import *
import os, sys

class Translator:
    def __init__(self, indoDict="../data/indonesia.txt", sundaDict="../data/sunda.txt"):
        self.libparser = LibParser(indo = indoDict, sunda = sundaDict)
        self.text = []
        self.translation = []

    def setText(self, text):
        self.text = inputParser.prefixSeparator(text.split(" "))
        self.text = inputParser.suffixSeparator(self.text)
        self.textLength = len(self.text)
        return self

    def getTranslation(self):
        return " ".join(self.translation)

    def translate(self, type, method="kmp"):
        if(method == "kmp"):
            matcher = KMPMatcher()
        elif(method == "bm"):
            matcher = BoyerMooreMatcher()
        else: # method == "regex"
            matcher = RegexMatcher()

        if(type == "sunda-indo"):
            dictionary = self.libparser.vocabSunda
        else: # type == "indo-sunda"
            dictionary = self.libparser.vocabIndo
        
        i, dictLength = 0, len(dictionary)
        while(i < self.textLength):
            if(type == "sunda-indo" and \
                self.libparser.isSpecialWord(self.text[i], type)):
                i += 1
            else:
                textToValidate, result = "", ""
                j, k, isFound = 0, 0, False
                while(not isFound and j < dictLength):
                    k = dictionary[j].keyLength
                    textToValidate = " ".join(self.text[i : min([i + k, self.textLength])])
                    # print(textToValidate +  ' ' + dictionary[j].key + ' ' + str(k))
                    isFound = matcher.setText(dictionary[j].key)\
                                        .setPattern(textToValidate)\
                                        .match()
                    if(not isFound):
                        j += 1
                temp = []
                if(not isFound):
                    temp = self.text[i : min([i + k, self.textLength])]
                    i += 1
                else:
                    temp = dictionary[j].data.split(" ")
                    i += k
                for word in temp:
                    self.translation.append(word)
        # print(self.translation)
        return " ".join(self.translation)

if __name__=='__main__':
    t = Translator()
    a = "nami abdi Riyugan"
    # t.setText(a).translate("indo-sunda")
    t.setText(a)
    print(t.text)
    print(t.textLength)
    print(t.setText(a).translate("sunda-indo"))


