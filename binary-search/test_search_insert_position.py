# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
# would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2

def searchInsert(nums, target):
    leftIndex = 0
    rightIndex = len(nums) - 1

    while leftIndex <= rightIndex:
        middle = int((leftIndex + rightIndex) / 2)

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            leftIndex = middle + 1
        else:
            rightIndex = middle - 1

    return leftIndex

def test_searchInsert():
    assert searchInsert([1,3,5,6], 5) == 2


print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))