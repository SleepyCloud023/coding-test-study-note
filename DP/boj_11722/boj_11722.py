# https://www.acmicpc.net/problem/11722
# title: 가장 긴 감소하는 부분 수열
# start: 2022-03-21 09:14:04 AM
# end:   2022-03-21 09:26:04 AM

def solution(N: int, arr: list):
    # 0...N-1
    # i번째 원소를 골랐을때 만들 수 있는 가장 긴 감소수열의 길이
    dp = [0] * N

    # 0...N-1
    for i in range(N):
        cur_number = arr[i]
        # 0부터 i-1번째 원소를 골랐을 때 만들 수 있는 가장 긴 감소 수열의 길이
        for prev in range(i):
            prev_number = arr[prev]
            if prev_number > cur_number:
                dp[i] = max(dp[i], dp[prev])
        dp[i] += 1

    return max(dp)


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    result = solution(N, arr)
    print(result)
