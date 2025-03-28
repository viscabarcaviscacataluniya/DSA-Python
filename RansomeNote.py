from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for char in ransomNote:
            if counter[char]>0:
                counter[char] -= 1
            else:
                return False
        return True         