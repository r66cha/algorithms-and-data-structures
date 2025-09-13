class SearchAlgorithms:

    def linear_three_min_elements(self, nums: list):
        N = len(nums)
        M, smallM, smallM2 = [2 * 1e9] * 3
        for el in nums:
            if el < M:
                smallM = M
                smallM2 = smallM
                M = el
            elif el < smallM:
                smallM2 = smallM
                smallM = el
            elif el < smallM2:
                smallM2 = el

        return M, smallM, smallM2

    def bin_search(self, nums: list, target: int):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


nums = [1, 2, 3, 4, 5, 6, 7, 8]
s = SearchAlgorithms()
print(s.bin_search(nums, 2))
