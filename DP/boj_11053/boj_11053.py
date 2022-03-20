# https://www.acmicpc.net/problem/11053
# title: 가장 긴 증가하는 부분 수열
# start: 2022-03-20 10:58:59 PM
# end:   2022-03-20 12:38:59 PM

def solution(N, arr):
    # i번째 자리를 골랐을 때 만들수 있는 가장 큰 증가수열의 길이
    dp = [0] * (N+1)

    # 1 ... N
    for cur in range(1, N + 1):
        for j in range(cur):
            if arr[j] < arr[cur]:
                dp[cur] = max(dp[cur], dp[j])

        dp[cur] += 1

    return max(dp)


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    result = solution(N, [0] + arr)
    print(result)
