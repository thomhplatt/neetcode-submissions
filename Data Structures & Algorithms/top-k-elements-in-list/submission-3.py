class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in seen:
            index = seen[num]
            buckets[index].append(num)

        result = []
        for i in reversed(buckets):
            if len(result) < k:
                result.extend(i)
                
        return result





