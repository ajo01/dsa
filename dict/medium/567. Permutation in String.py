# dict string 



# use counter to optimize

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        n2 = len(s2)

        if n > n2:
            return False

        counter = Counter(s1)

        for i in range(n2 - n + 1):
            tmp = s2[i:i+n]
            counter2 = Counter(tmp)
            flag = True
            for k in counter:
                if k not in counter2 or counter[k] != counter2[k]:
                    flag = False
            if flag is True:
                return True
        return False



# not optimized

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       
        d1 = {}

        n = len(s1)
        n2 = len(s2)

        if n > n2:
            return False

        for i in range(n):
            if s1[i] in d1:
                d1[s1[i]] += 1
            else:
                d1[s1[i]] = 1

        for i in range(n2 - n + 1):
            d2 = {}
            for j in range(i, i+n):
                if s2[j] in d2:
                    d2[s2[j]] += 1
                else:
                    d2[s2[j]] = 1
            flag = True
            for k in d1:
                if k not in d2 or d1[k] != d2[k]:
                    flag = False
            if flag is True:
                return True
        return False

