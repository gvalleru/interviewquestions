class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def product_except_self(self):
        sol = [1] * len(self.nums)
        product = self.nums[0]
        for i in range(1, len(self.nums)):
            sol[i] *= product
            product *= self.nums[i]

        product = self.nums[-1]
        for i in range(len(self.nums) - 2, -1, -1):
            sol[i] *= product
            product *= self.nums[i]
            
        return sol


if __name__ == "__main__":
    input_ = [2, 3, 4, 5]
    x = Solution(input_)
    print x.product_except_self()
