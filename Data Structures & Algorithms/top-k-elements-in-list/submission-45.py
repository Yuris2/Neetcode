import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Count the occurences of each number
        count = Counter(nums)
        #Create a bucket for the number of times an elem can occur
        occ = [[] for _ in range(len(nums) + 1)]
        #Fill the buckets with elements from the counter
        for n, cnt in count.items():
            occ[cnt].append(n)
        #Using buckets, go backwards to find top k elements
        res = []

        for bucket in reversed(occ):
            for item in bucket:
                res.append(item)

                if len(res) == k:
                    return res
        
        return res
      