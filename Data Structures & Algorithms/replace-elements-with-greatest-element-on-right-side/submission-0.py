class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force

        # for i in range(len(arr)-1):
        #     k = arr[i+1]
        #     for j in range(i+2, len(arr)):
        #         if k < arr[j]:
        #             k = arr[j]
        #     arr[i]=k
        # arr[len(arr)-1] = -1
        # return arr
        # -----------------------------------------

        #running max suffix rightMax

        n = len(arr)
        ans = [0] * n
        rightMax = -1
        i = n-1
        while i > -1:
            ans[i] = rightMax
            rightMax = max(rightMax, arr[i])
            i -=1
        return ans







