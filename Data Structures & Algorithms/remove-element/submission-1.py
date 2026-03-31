class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #  my initial approach
        # a = 0
        # i = 0
        # n = len(nums)
        # while i < n:
        #     if nums[i] == val:
        #         a +=1
        #         for j in range(i+1,n,1):
        #             nums[j-1]= nums[j]
        #         n -=1
        #     else:
        #         i += 1
        # return len(nums)-a
        # ------------------------------------------------------------
        # brute force

        # tmp = []
        # i = 0
        # for num in nums:
        #     if num != val:
        #         tmp.append(num)
        # for num in tmp:
        #     nums[i] = num
        #     i += 1
        # return len(tmp)
        # ----------------------------------------------------------

        # two pointer - copy
        # k = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k] = nums[i]
        #         k += 1
        # return k
        # -----------------------------------------------------------

        # two pointer - swap
        i = 0
        k = len(nums)
        while i<k:
            if nums[i] == val:
                nums[i]=nums[k-1]
                k -= 1
            else:
                i += 1
        return k

        