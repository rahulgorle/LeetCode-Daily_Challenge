class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        i = 0  # Pointer for the target array
        num = 1  # Current number in the stream

        while i < len(target):
            t = target[i]
            while num < t:
                # Push integers from the stream to the stack until you reach t
                result.extend(["Push", "Pop"])
                num += 1
            # At this point, num == t, so you can simply Push t to the stack
            result.append("Push")
            i += 1
            num += 1

        return result
