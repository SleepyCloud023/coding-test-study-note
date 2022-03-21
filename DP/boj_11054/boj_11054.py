# https://www.acmicpc.net/problem/11054
# title: 가장 긴 바이토닉 부분 수열
# start: 2022-03-21 09:30:29 AM
# end:   2022-03-21 09:46:29 AM


def solution(N: int, arr: list):
    dp_asc = [0] * N
    dp_desc = [0] * N

    for i in range(N):
        cur_number = arr[i]
        for idx_prev in range(i):
            prev_number = arr[idx_prev]

            if cur_number > prev_number:
                dp_asc[i] = max(dp_asc[i], dp_asc[idx_prev])
        dp_asc[i] += 1

    # N-1 ... 0
    for i in range(N-1, -1, -1):
        cur_number = arr[i]
        for idx_next in range(i+1, N):
            next_number = arr[idx_next]

            if cur_number > next_number:
                dp_desc[i] = max(dp_desc[i], dp_desc[idx_next])

        dp_desc[i] += 1

    return max([left + right - 1 for (left, right) in zip(dp_asc, dp_desc)])


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    result = solution(N, arr)
    print(result)
