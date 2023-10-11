class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        ans=[0]*len(people)
        flower_bloom_start=[x[0] for x in sorted(flowers,key=lambda x:x[0])]
        flower_bloom_end=[x[1]+1 for x in sorted(flowers,key=lambda x:x[1])]
        def binary_search(array,date):
            low,high=0,len(array)
            while low<high:
                mid=(low+high)//2

                if array[mid]>date:
                    high=mid
                else:
                    low=mid+1
            return low
        for i in range(len(people)):
            a=binary_search(flower_bloom_start,people[i])
            b=binary_search(flower_bloom_end,people[i])
            ans[i]=a-b
        return ans

        
