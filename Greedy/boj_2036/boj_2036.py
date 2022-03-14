# https://www.acmicpc.net/problem/2036
# 수열과 점수
# 11: 58 start
# 12: 26 end => 반례 케이스 찾아서 봄: 양수가 1인 경우 예외처리

import sys
input = sys.stdin.readline


def solution(num_zero: int, plus_list: list, minus_list: list) -> int:
    plus_list.sort()
    # -1 -2 -3 -4 -5
    minus_list.sort(reverse=True)

    point = 0

    while(len(plus_list) >= 2):
        big_1 = plus_list.pop()
        big_2 = plus_list.pop()
        point += big_1 * big_2

        if big_1 == 1 or big_2 == 1:
            point += 1

    if plus_list:
        point += plus_list[0]

    while(len(minus_list) >= 2):
        small_1 = minus_list.pop()
        small_2 = minus_list.pop()
        point += small_1 * small_2

    if num_zero == 0:
        point += sum(minus_list)

    return point


if __name__ == '__main__':
    N = int(input())
    plus_list, minus_list = [], []
    num_zero = 0
    for _ in range(N):
        number = int(input())
        if number == 0:
            num_zero += 1
        elif number > 0:
            plus_list.append(number)
        elif number < 0:
            minus_list.append(number)

    result = solution(num_zero, plus_list, minus_list)
    print(result)
