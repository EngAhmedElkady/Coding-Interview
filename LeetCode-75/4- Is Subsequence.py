class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return 1

        num = 0
        l = 0
        for i in range(len(s)):
            for y in range(l, len(t)):
                if s[i] == t[y]:
                    l = y+1
                    num += 1
                    break
        if len(s) == num:
            return 1
        return 0
