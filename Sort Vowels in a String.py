class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        vowel_indices = [i for i, char in enumerate(s) if char in vowels]

        sorted_vowels = sorted([s[i] for i in vowel_indices])

        result = list(s)
        for i, v_index in enumerate(vowel_indices):
            result[v_index] = sorted_vowels[i]

        return ''.join(result)
