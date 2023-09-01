#!/usr/bin/python
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        for key in ransom:
            if ransom[key] > mag[key]:
                return False
        return True


s = Solution()

print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
print(s.canConstruct("aab", "baa"))
print(s.canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))
