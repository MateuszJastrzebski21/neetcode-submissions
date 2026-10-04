class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        res = []

        for n in nums:
            count[n] = count.get(n, 0) + 1

        buckets = [[] for i in range(len(nums) +1)]

        for n, c in count.items():
            buckets[c].append(n)

        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res


