#!/usr/bin/python

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = list(magazine)
        for char in ransomNote:
            if char in mag:
                mag.remove(char)
            else:
                return False
        return True

s = Solution()

print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
print(s.canConstruct("aab", "baa"))
