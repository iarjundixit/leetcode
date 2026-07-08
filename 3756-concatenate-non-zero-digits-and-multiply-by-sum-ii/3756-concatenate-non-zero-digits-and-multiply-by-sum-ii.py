class Solution(object):
    def sumAndMultiply(self, s, queries):
        # MOD = 10**9 + 7
        # ans = []

        # for l, r in queries:

        #     num = 0
        #     digit_sum = 0

        #     for i in range(l, r + 1):

        #         if s[i] != '0':
        #             digit = int(s[i])

        #             num = num * 10 + digit
        #             digit_sum += digit

        #     ans.append((num * digit_sum) % MOD)

        # return ans        
        MOD = 10**9 + 7
        n = len(s)

        # powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix arrays
        sum_d = [0] * (n + 1)
        cnt_n0 = [0] * (n + 1)
        p = [0] * (n + 1)

        for i in range(1, n + 1):
            d = int(s[i - 1])

            sum_d[i] = sum_d[i - 1] + d
            cnt_n0[i] = cnt_n0[i - 1] + (d > 0)

            if d:
                p[i] = (p[i - 1] * 10 + d) % MOD
            else:
                p[i] = p[i - 1]

        ans = []

        for l, r in queries:

            n0 = cnt_n0[r + 1] - cnt_n0[l]

            digit_sum = sum_d[r + 1] - sum_d[l]

            x = (p[r + 1] - p[l] * pow10[n0]) % MOD

            ans.append((x * digit_sum) % MOD)

        return ans