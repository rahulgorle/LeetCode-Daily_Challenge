class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Ensure sentence1 is always the longer sentence (or equal length)
        if len(sentence1) < len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        
        # Split both sentences into words
        words1 = sentence1.split()
        words2 = sentence2.split()

        i, j = 0, 0
        # Check prefix matches
        while i < len(words2) and words1[i] == words2[i]:
            i += 1

        # Check suffix matches
        while j < len(words2) - i and words1[-1 - j] == words2[-1 - j]:
            j += 1

        # The two sentences are similar if the total number of matched words equals the length of the shorter sentence
        return i + j == len(words2)
