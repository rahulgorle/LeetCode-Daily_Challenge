class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Iterate through the digits from right to left
        for i in range(len(num) - 1, -1, -1):
            # Check if the current substring is odd
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        # If no odd number is found, return an empty string
        return ""
