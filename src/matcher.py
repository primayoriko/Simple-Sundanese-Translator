import re, sys

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
        self.pattern = pattern
        self.patLength = len(pattern)
        return self

    def solver(self, findAll = False):
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

    def findPattern(self, findAll = False):
        # self.resultIdx = []
        if(self.patLength != self.textLength):
            return False
        lookback = self.initLookbackArray()
        i, j = self.patLength - 1, self.patLength - 1
        while(i < self.textLength):
            if(self.pattern[j] == self.text[i]):
                if(j == 0):
                    self.resultIdx.append(i)
                    if(not findAll):
                        break
                    i, j = i + self.patLength, self.patLength - 1
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
        return self.resultIdx

class KMPMatcher(Matcher):
    def __init__(self):
        super().__init__()

    def initKMPBorder(self):
        KMPBorder = [-1] * self.patLength
        KMPBorder[0] = 0
        i, j = 1, 0
        while(i < self.patLength):
            if(self.pattern[i] == self.pattern[j]):
                KMPBorder[i] = j + 1
            elif(j > 0):
                j = KMPBorder[j - 1]
            else:
                KMPBorder[i]= 0
                i += 1
        return KMPBorder

    def findPattern(self, findAll = False):
        # self.resultIdx = []
        if(self.patLength != self.textLength):
            return False
        KMPBorder = self.initKMPBorder()
        i, j = 0, 0
        while(i < self.textLength):
            if(self.pattern[j] == self.text[i]):
                if(j == self.patLength - 1):
                    self.resultIdx.append(i - self.patLength + 1)
                    if(not findAll):
                        break
                    i, j = i + 1, KMPBorder[j] 
                else:
                    i, j = i + 1, j + 1
            else:
                if(j > 0):
                    j = KMPBorder[j - 1]
                else:
                    i += 1
        return self.resultIdx

class RegexMatcher(Matcher):
    def __init__(self):
        super().__init__()

    def findPattern(self, findAll = False):
        if(self.patLength != self.textLength):
            return False
        self.resultIdx = re.findall(self.pattern, self.text)
        return self.resultIdx

if __name__ == '__main__':
    pattern = "abc"
    text = "reabcasdsabcasdaabcb"
    matcher = BoyerMooreMatcher(text = text, pattern=pattern)
    matcher.solver()
    # print(len)
    print(matcher.resultIdx)
    # print(matcher.initLookbackArray())
    matcher.printSolution()
    matcher2 = KMPMatcher(text = text, pattern=pattern)
    matcher2.solver()
    # print(len)
    print(matcher2.resultIdx)
    matcher3 = RegexMatcher(text = text, pattern=pattern)
    matcher3.solver()
    # print(len)
    print(matcher3.resultIdx)
    pass

