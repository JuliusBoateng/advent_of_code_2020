#!/usr/bin/env python3
import sys

def sum_to_2020(lines, nums):
    if not lines:
        return 0

    if len(nums) > 3:
        return 0

    if (len(nums) == 3) and (sum(nums) == 2020):
        return nums[0] * nums[1] * nums[2]

    val = lines[0]
    
    result_1 = sum_to_2020(lines[1:], nums + [val])
    result_2 = sum_to_2020(lines[1:], nums)

    return result_1 if result_1 > 0 else result_2

    # for index_1 in range(len(lines) - 1):
    #     for index_2 in range(index_1, len(lines)):
    #         if (lines[index_1] + lines[index_2]) == 2020:
    #             return lines[index_1] * lines[index_2]

def main():
    lines = list(map(lambda num: int(num.strip()),sys.stdin))
    print(sum_to_2020(lines,[]))


if __name__ == "__main__":
    main()