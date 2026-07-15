class Solution(object):
    def removeElement(self, nums, val):
        # for i in nums[:]:
        #     if i == val:
        #         nums.remove(i)

            
        # k = len(nums)
        # return k 
        # optimal approach 

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
            
        