class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        for i in range(len(s) - 1, 0, -1):
            if s[i] == '1':
                if carry == 1:
                    steps += 1  # Current bit is 1 and we already have a carry
                else:
                    carry = 1
                    steps += 2  # We need to add 1 to make this 0 and carry over
            else:  # s[i] == '0'
                if carry == 1:
                    steps += 2  # Current bit is 0 and we have a carry
                else:
                    steps += 1  # Simply divide by 2
                
        # Finally, if we still have a carry, it means we need one more step to turn '1' to '0' and carry over
        if carry == 1:
            steps += 1
        
        return steps
