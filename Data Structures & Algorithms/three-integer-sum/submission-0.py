class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i , a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            i, j = i + 1, len(nums) -1
            while i < j:
                threeSum = a + nums[i] + nums[j]
                if threeSum > 0:
                    j -=1
                elif threeSum < 0:
                    i +=1
                else:
                    res.append ([a, nums[i], nums[j]])
                    i +=1
                    while nums[i] == nums [i - 1] and i < j:
                        i +=1
        return res
                
        