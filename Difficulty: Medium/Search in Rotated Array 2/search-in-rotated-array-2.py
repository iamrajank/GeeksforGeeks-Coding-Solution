#User function Template for python3

class Solution:
    def Search(self, nums, target):
        # code here
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            elif nums[l] == nums[mid] and nums[mid] == nums[r]:
                l = l + 1
                r = r - 1
                continue
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.Search(arr, k)
        if res:
            print("true")
        else:
            print("false")
        print("~")
        t -= 1

# } Driver Code Ends