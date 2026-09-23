class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myhash = {} 
        count = Counter(nums) #(number, frequency) (key, value)

        result = []

        for num, freq in count.most_common(k): #count.most_common(k) = top k most common 
            result.append(num)
        return result



        
        
