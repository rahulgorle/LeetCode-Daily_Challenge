class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # Split the input string into words
        reversed_words = [word[::-1] for word in words]  # Reverse each word
        result = ' '.join(reversed_words)  # Join the reversed words with spaces
        return result
