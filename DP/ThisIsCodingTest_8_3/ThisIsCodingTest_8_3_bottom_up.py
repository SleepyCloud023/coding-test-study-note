# BinarySearch/8_3
# title: 개미전사
# start: 2022-03-19 11:28:14 PM
# end:   2022-03-19 11:28:14 PM

import sys
input = sys.stdin.readline


def count(value_list: list, N: int):
    idx = 2
    left_2 = value_list[0]
    left_1 = max(left_2, value_list[1])
    current = max(left_2 + value_list[idx], left_1)

    while(idx < N):
        current = max(left_2 + value_list[idx], left_1)
        left_2 = left_1
        left_1 = current
        idx += 1

    return current


if __name__ == '__main__':
    N = int(input())
    value_list = list(map(int, input().split()))
    dp = [0] * N
    result = count(value_list, N)
    print(result)
