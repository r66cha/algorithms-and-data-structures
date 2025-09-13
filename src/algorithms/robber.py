class Solution:
    def max_rob(self, houses: list[int]) -> int:
        if not houses:
            return 0
        elif len(houses) == 1:
            return houses[0]

        N = len(houses)
        dp = [0] * N
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])

        for i in range(2, N):
            dp[i] = max(dp[i - 1], houses[i] + dp[i - 2])

        return dp[-1]


s = Solution()
print(s.max_rob([1, 7, 5, 3]))
