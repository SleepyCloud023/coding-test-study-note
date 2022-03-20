# https://www.acmicpc.net/problem/1904
# title: 01타일
# start: 2022-03-20 06:05:56 AM
# end:   2022-03-20 06:38:56 AM

def fibo(N):
    dp = [0] * (3 + abs(N-2))
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N + 1):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746

    return dp[N] % 15746


N = int(input())
print(fibo(N))
