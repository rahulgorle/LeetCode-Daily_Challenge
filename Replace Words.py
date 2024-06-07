class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search_shortest_prefix(self, word):
        node = self.root
        prefix = []
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefix.append(char)
            if node.is_end:
                return ''.join(prefix)
        return word

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        trie = Trie()
        
        # Insert all roots into the trie
        for root in dictionary:
            trie.insert(root)
        
        # Split the sentence into words
        words = sentence.split()
        
        # Replace words with their shortest root found in the trie
        replaced_words = [trie.search_shortest_prefix(word) for word in words]
        
        # Join the words back into a sentence
        return " ".join(replaced_words)
