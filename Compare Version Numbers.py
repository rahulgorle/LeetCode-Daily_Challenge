class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        # Iterate through the maximum number of revisions in both versions
        for i in range(max(len(v1), len(v2))):
            # Get the i-th revision of both versions, defaulting to 0 if not present
            rev1 = int(v1[i]) if i < len(v1) else 0
            rev2 = int(v2[i]) if i < len(v2) else 0
            
            # Compare the revisions
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        # If all revisions are equal, return 0
        return 0
