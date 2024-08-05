class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Step 1: Count the occurrences of each string
        count = {}
        for string in arr:
            if string in count:
                count[string] += 1
            else:
                count[string] = 1
        
        # Step 2: Collect the k-th distinct string
        distinct_count = 0
        for string in arr:
            if count[string] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return string
        
        return ""
