class Solution:
    def maxScoreWords(self, words, letters, score):
        from collections import Counter

        # Create a frequency counter for the given letters
        letter_count = Counter(letters)
        
        # Helper function to calculate the score of a given word
        def get_word_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)
        
        # Backtracking function to find the maximum score
        def backtrack(index, current_score, available_letters):
            if index == len(words):
                return current_score
            
            max_score = current_score
            
            # Skip the current word
            max_score = max(max_score, backtrack(index + 1, current_score, available_letters))
            
            # Try to include the current word if possible
            word = words[index]
            word_count = Counter(word)
            
            if all(word_count[char] <= available_letters[char] for char in word_count):
                # Update the available letters
                for char in word_count:
                    available_letters[char] -= word_count[char]
                
                # Recur with the current word included
                max_score = max(max_score, backtrack(index + 1, current_score + get_word_score(word), available_letters))
                
                # Backtrack: restore the available letters
                for char in word_count:
                    available_letters[char] += word_count[char]
            
            return max_score
        
        # Start backtracking from index 0, initial score 0, and the available letters
        return backtrack(0, 0, letter_count)
