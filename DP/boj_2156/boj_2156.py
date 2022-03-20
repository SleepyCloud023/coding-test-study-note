# https://www.acmicpc.net/problem/2156
# title: 포도주 시식
# start: 2022-03-20 10:13:26 PM
# end:   2022-03-20 10:35:26 PM

def solution(N, wine):
    # 3 x N
    dp = [[0] * 3 for _ in range(N)]
    dp[0] = [0, wine[0], wine[0]]

    # 0 .... N-2
    for i in range(N - 1):
        # i+1번째 와인
        prev_0 = dp[i][0]
        prev_1 = dp[i][1]
        prev_2 = dp[i][2]

        dp[i+1][0] = max(prev_0, prev_1, prev_2)
        dp[i+1][1] = prev_0 + wine[i+1]
        dp[i+1][2] = prev_1 + wine[i+1]

    return max(dp[N-1])


if __name__ == '__main__':
    N = int(input())

    wine = []
    for _ in range(N):
        wine.append(int(input()))

    result = solution(N, wine)
    print(result)
