class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Initialize two pointers for the sliding window
        left, right = 0, 0

        # HashMap to store characters in t and their counts
        target_count = {}
        for char in t:
            target_count[char] = target_count.get(char, 0) + 1

        # Variables to track the minimum window substring
        min_len = float('inf')
        min_window = ""

        # Number of characters in t that are still needed to be matched
        required_chars = len(target_count)

        # Iterate through the string s using the right pointer
        while right < len(s):
            # Check if the current character is in t
            if s[right] in target_count:
                target_count[s[right]] -= 1
                if target_count[s[right]] == 0:
                    required_chars -= 1

            # Move the left pointer to minimize the window
            while required_chars == 0:
                # Update the minimum window substring
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]

                # Check if the left character is in t
                if s[left] in target_count:
                    target_count[s[left]] += 1
                    if target_count[s[left]] > 0:
                        required_chars += 1

                # Move the left pointer to the right
                left += 1

            # Move the right pointer to the right
            right += 1

        return min_window
