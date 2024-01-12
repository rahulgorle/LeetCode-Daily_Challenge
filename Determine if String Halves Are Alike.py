class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowels(string):
            vowels = set('aeiouAEIOU')
            return sum(1 for char in string if char in vowels)

        length = len(s)
        mid_point = length // 2
        vowels = set('aeiouAEIOU')

        count_first_half = sum(1 for i in range(mid_point) if s[i] in vowels)
        count_second_half = sum(1 for i in range(mid_point, length) if s[i] in vowels)

        return count_first_half == count_second_half
