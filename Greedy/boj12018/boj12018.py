# https://www.acmicpc.net/problem/12018
# Yonsei TOTO

import sys
input = sys.stdin.readline


def get_min_point(num_limit: int, num_currernt: int, current_point_list: list):
    if num_currernt < num_limit:
        return 1

    current_point_list.sort(reverse=True)
    target_point = current_point_list[num_limit-1]
    return target_point


def count_max_subject(min_point_list: list, M):
    min_point_list.sort()
    result = 0
    for point in min_point_list:
        if M - point >= 0:
            result += 1
            M -= point
        else:
            break
    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    min_point_list = []

    for _ in range(N):
        num_current, num_limit = map(int, input().split())
        current_point_list = list(map(int, input().split()))
        min_point_list.append(get_min_point(
            num_limit, num_current, current_point_list))

    min_point_list.sort()
    result = count_max_subject(min_point_list, M)
    print(result)
