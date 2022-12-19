

def sort(nums):
    for i in range(len(nums)-1):
        minpos=i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
               minpos=j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums=[5,1,8,7,6,2]
sort(nums)
print(nums)

