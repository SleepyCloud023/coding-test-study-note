# https://www.acmicpc.net/problem/10844
# title: 쉬운 계단 수
# start: 2022-03-20 09:55:30 PM
# end:   2022-03-20 10:12:30 PM

def solution(N):
    # 0 ... N
    # k 길이 중 i로 끝나는 계단수의 갯수
    dp = [[0] * 10 for _ in range(N+1)]
    dp[1] = [0] + [1] * 9

    for i in range(2, N+1):
        for number in range(10):
            prev, next = number - 1, number + 1
            if prev >= 0:
                dp[i][number] += dp[i-1][prev]

            if next <= 9:
                dp[i][number] += dp[i-1][next]

            dp[i][number] %= int(1e9)

    return sum(dp[N]) % int(1e9)


if __name__ == '__main__':
    N = int(input())
    result = solution(N)
    print(result)
