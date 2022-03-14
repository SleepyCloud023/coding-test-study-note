# https://www.acmicpc.net/problem/1911
# 흙길 보수하기

import sys
input = sys.stdin.readline

# 4:20 start
# 4:42 end => 22분


def solution(pond_list: list) -> int:
    count = 0
    pond_list.sort()
    next_start = 0
    for (start, end) in pond_list:
        start = max(next_start, start)
        if start > end:
            continue
        elif start < end:
            num_L = (end - start - 1) // L + 1
            next_start = start + L * num_L
            count += num_L
    return count


if __name__ == '__main__':
    N, L = map(int, input().split())
    pond_list = []
    for _ in range(N):
        pond = tuple(map(int, input().split()))
        pond_list.append(pond)
    result = solution(pond_list)
    print(result)
