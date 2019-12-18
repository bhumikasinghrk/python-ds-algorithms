
def largest_number_at_least_twice_of_others(nums: [int]) -> int:
    """
    Find largest number that is atleast twice the size of any other number
    :param nums: array of numbers
    :return: index of number, -1 if none exists
    """
    largest = None
    next_largest = None

    for idx, num in enumerate(nums):
        if largest is None:
            largest = idx
            continue
        if num > nums[largest]:
            next_largest = largest
            largest = idx
            continue
        if next_largest is None or num > nums[next_largest]:
            next_largest = idx

    if next_largest is None or (nums[next_largest] * 2) <= nums[largest]:
        return largest
    return -1


def largest_number_at_least_twice_of_others2(nums: [int]) -> int:
    """
    Find largest number that is atleast twice the size of any other number
    :param nums: array of numbers
    :return: index of number, -1 if none exists
    """
    if len(nums) == 1:
        return 0

    max_index = nums.index(max(nums))
    max_val = nums.pop(max_index)
    next_max = max(nums)

    if next_max * 2 <= max_val:
        return max_index
    return -1
