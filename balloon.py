from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = "balloon"
        counter = Counter(text)
        return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2,counter['n'])
