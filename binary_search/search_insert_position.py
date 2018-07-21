# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
# would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2

def search_insert(nums, target):
    leftindex = 0
    rightindex = len(nums) - 1

    while leftindex <= rightindex:
        middle = int((leftindex + rightindex) / 2)

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            leftindex = middle + 1
        else:
            rightindex = middle - 1

    return leftindex