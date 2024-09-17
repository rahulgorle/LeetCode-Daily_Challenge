class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s3 = s1 + ' ' + s2
        l3 = list(s3.split(' '))
        result = []
        for i in range(len(l3)):
            if l3.count(l3[i]) < 2:
                result.append(l3[i])
        return result
