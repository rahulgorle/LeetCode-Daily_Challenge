class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        max_score = current_score = left = 0
        right = len(tokens) - 1

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                current_score += 1
                max_score = max(max_score, current_score)
            elif current_score > 0:
                power += tokens[right]
                right -= 1
                current_score -= 1
            else:
                break

        return max_score
