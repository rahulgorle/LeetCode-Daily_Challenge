class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        hashmap = {0: -1}

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in hashmap:
                max_length = max(max_length, i - hashmap[count])
            else:
                hashmap[count] = i

        return max_length
