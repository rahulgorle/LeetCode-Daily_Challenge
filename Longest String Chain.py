class Solution:
    def longestStrChain(self, words):
        # Sort the words by their length in ascending order
        words.sort(key=len)
        
        # Create a dictionary to store the length of the longest chain for each word
        word_chain_length = {}
        
        max_chain_length = 1
        
        for word in words:
            # Initialize the chain length for the current word to 1
            word_chain_length[word] = 1
            
            # Try removing each character from the word and check if it exists in the dictionary
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in word_chain_length:
                    word_chain_length[word] = max(word_chain_length[word], word_chain_length[prev_word] + 1)
            
            # Update the maximum chain length
            max_chain_length = max(max_chain_length, word_chain_length[word])
        
        return max_chain_length
