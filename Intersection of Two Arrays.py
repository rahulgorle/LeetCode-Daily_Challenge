class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a set for faster lookup
        set1 = set(nums1)
        
        # Use list comprehension to find the intersection
        return list({x for x in nums2 if x in set1})
