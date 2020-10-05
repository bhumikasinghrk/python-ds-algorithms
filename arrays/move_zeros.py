from typing import List


def move_zeros(nums: List[int]) -> None:
    length = len(nums)

    read_index = 0
    write_index = 0

    while read_index < length:
        if nums[read_index] != 0:
            nums[write_index] = nums[read_index]
            write_index += 1
        read_index += 1

    while write_index < read_index:
        nums[write_index] = 0
        write_index += 1
