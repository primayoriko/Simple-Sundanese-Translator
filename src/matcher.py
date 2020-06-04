import re, sys

class Matcher:
    # def __init__(self, text = "", pattern = "-"):
    def __init__(self):
        self.text, self.pattern = "", ""
        self.textLength, self.patLength = len(self.text), len(self.pattern)

    def setText(self, text):
        self.text = text
        self.textLength = len(text)
        return self

    def setPattern(self, pattern):
        self.pattern = pattern
        self.patLength = len(pattern)
        return self

    def matcher(self):
        # function to find out if the pattern and text is exact
        # and return the boolean and the translation result 
        return False

class BoyerMooreMatcher(Matcher):
    def __init__(self):
        super().__init__()
        
    def initLookbackArray(self):
        # Find last occurence of a char in the pattern, if not found then -1
        lookback = [-1] * 256
        for i in range(self.patLength):
            lookback[ord(self.pattern[i])] = i
        return lookback

    def match(self):
        if(self.patLength != self.textLength):
            return False
        lookback = self.initLookbackArray()
        i, j = self.patLength - 1, self.patLength - 1
        while(i < self.textLength):
            if(self.pattern[j] == self.text[i]):
                if(j == 0):
                    return True
                    # i, j = i + self.patLength, self.patLength - 1
                else:
                    i, j = i - 1, j - 1
            else:
                lookback_val = lookback[ord(self.text[i])]
                i = i + self.patLength - min(j, 1 + lookback_val)
                j = self.patLength - 1
                # if(lookback_val < j and lookback_val != -1):
                #     j = lookback_val
                # else:
                #     i, j = i + self.patLength, self.patLength - 1
        return False

class KMPMatcher(Matcher):
    def __init__(self):
        super().__init__()

    def initKMPBorder(self):
        KMPBorder = [0] * self.patLength
        KMPBorder[0] = 0
        i, j = 1, 0
        while(i < self.patLength):
            # print(str(i)+' '+str(j)+' '+self.pattern[i]+self.pattern[j])
            if(self.pattern[i] == self.pattern[j]):
                j += 1
                KMPBorder[i] = j
                i += 1
            elif(j > 0):
                j = KMPBorder[j - 1]
            else:
                KMPBorder[i] = 0
                i += 1
        return KMPBorder

    def match(self):
        if(self.patLength != self.textLength):
            return False
        KMPBorder = self.initKMPBorder()
        i, j = 0, 0
        while(i < self.textLength):
            if(self.pattern[j] == self.text[i]):
                if(j == self.patLength - 1):
                    return True
                    # i, j = i + 1, KMPBorder[j] 
                else:
                    i, j = i + 1, j + 1
            else:
                if(j > 0):
                    j = KMPBorder[j - 1]
                else:
                    i += 1
        return False

class RegexMatcher(Matcher):
    def __init__(self):
        super().__init__()

    def match(self):
        # if(self.patLength != self.textLength):
        #     return False
        return len(re.findall(self.pattern, self.text)) == 1

if __name__ == '__main__':
    pattern = "nama saya Riyugan"
    text = "berasal dari mana"

    kmp = KMPMatcher().setPattern(pattern).setText(text)
    # print(kmp.text)
    # print(kmp.pattern)
    if(kmp.match()):
        print("KMP")
    else:
        print("wtf_KMP")

    bm = BoyerMooreMatcher().setPattern(pattern).setText(text)
    if(bm.match()):
        print("BM")
    else:
        print("wtf_BM")

    reg = RegexMatcher().setPattern(pattern).setText(text)
    if(reg.match()):
        print("Reg")
    else:
        print("wtf_Reg")
