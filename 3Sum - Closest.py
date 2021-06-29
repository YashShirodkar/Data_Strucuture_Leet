class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = sum(nums[:3])
        nums.sort()
        length = len(nums)
        for i in range(length -2):
            s = i+1
            e = length -1
            
            while s < e:
                sumhere = nums[i] +nums[s] + nums[e]
                
                if abs (sumhere- target) < abs(res - target):
                    res = sumhere
                if sumhere < target:
                    s += 1
                else :
                    e -= 1
                
        return res