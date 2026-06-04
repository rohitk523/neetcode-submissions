class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        dict1 = Counter(s)
        dict2 = Counter(t)
        if len(s)==len(t):
            for i in s:
                if dict1[i]!=dict2[i]:
                    return False
            return True
        else:
            return False
        