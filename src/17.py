def max_product_of_three(nums):
    if len(nums) < 3:
        return None
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
