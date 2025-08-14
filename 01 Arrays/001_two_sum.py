#Problem: Two Sum 
#Link: https://leetcode.com/problems/two-sum/
#Difficulty: Easy
#Approach: Use a dictionary to store the indices of the numbers we have seen so far.

# def two_sum(nums, target):
#     num_map = {}
#     for i, num in enumerate(nums):
#         diff = target - num
#         if diff in num_map:
#             return [num_map[diff], i]   
#         num_map[num] = i
#     return []
# print(two_sum([2, 7, 11, 15], 9))
def two_sums(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

nums = [2,7,11,15]
target = 9

two_sums(nums, target)