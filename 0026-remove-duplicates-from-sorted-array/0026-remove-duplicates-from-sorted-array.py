class Solution(object):
    def removeDuplicates(self, nums):
        # new = []
        # for num in nums:
        #   if num not in new:
        #      new.append(num)

        # k = len(new)
        # nums[:k] = new
        # return k 

        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1

        return k