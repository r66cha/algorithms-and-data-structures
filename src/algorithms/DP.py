class DP:

    mem = {1: 1, 2: 2}

    def f_dp(self, n: int):
        if n == 1 or n == 2:
            return n

        if n - 1 in self.mem:
            f1 = self.mem[n - 1]
        else:
            f1 = self.f_dp(n - 1)

        # --

        if n - 2 in self.mem:
            f2 = self.mem[n - 2]
        else:
            f2 = self.f_dp(n - 2)

        # --

        self.mem[n - 1] = f1
        self.mem[n - 2] = f2

        return f1 + f2


dp = DP()
print(dp.f_dp(4))
