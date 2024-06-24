class Solution:
    def minKBitFlips(self, nums, k):
        n = len(nums)
        flip = [0] * n
        flip_count = 0
        flips = 0
        
        for i in range(n):
            if i >= k:
                flip_count ^= flip[i - k]
            
            if (nums[i] ^ flip_count) == 0:
                if i + k > n:
                    return -1
                flip_count ^= 1
                flip[i] = 1
                flips += 1
                
        return flips
