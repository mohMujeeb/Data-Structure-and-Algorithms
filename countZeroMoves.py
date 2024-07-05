def count_zero_moves(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            count += 1
    return len(nums) - count

print(count_zero_moves([1, 2, 3, 4, 0, 0, 0, 0]))