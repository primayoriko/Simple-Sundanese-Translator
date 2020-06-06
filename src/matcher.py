import re, sys

class MatcherBuilder:
    @staticmethod
    def build(method="kmp"):
        if(method == "kmp"):
            matcher = KMPMatcher()
        elif(method == "bm"):
            matcher = BoyerMooreMatcher()
        else: # method == "regex"
            matcher = RegexMatcher()
        return matcher

class Matcher:
    # def __init__(self, text = "", pattern = "-"):
    def __init__(self):
        self.text, self.pattern = "", ""
        self.textLength, self.patLength = len(self.text), len(self.pattern)

    def setText(self, text):
        self.text = text.lower()
        self.textLength = len(text)
        return self

    def setPattern(self, pattern):
        self.pattern = pattern.lower()
        self.patLength = len(pattern)
        return self

    def match(self):
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
                else:
                    i, j = i - 1, j - 1
            else:
                lookback_val = lookback[ord(self.text[i])]
                i = i + self.patLength - min(j, 1 + lookback_val)
                j = self.patLength - 1
        return False

class KMPMatcher(Matcher):
    def __init__(self):
        super().__init__()

    def initKMPBorder(self):
        KMPBorder = [0] * self.patLength
        KMPBorder[0] = 0
        i, j = 1, 0
        while(i < self.patLength):
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
        return True if re.search("^" + self.pattern + "$", self.text) else False

if __name__ == '__main__':
    pattern = "he es"
    text = "?"

    kmp = KMPMatcher().setPattern(pattern).setText(text)
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
