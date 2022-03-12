# https://www.acmicpc.net/problem/2891
# 카약과 강풍

import sys
input = sys.stdin.readline


def get_left_idx(idx: int):
    return max(0, idx-1)


def get_right_idx(idx: int, N: int):
    return min(N, idx+1)


def solution(N: list, poor_list: list, rich_list: list):
    duplicate = set(poor_list) & set(rich_list)
    poor_list = [x for x in poor_list if x not in duplicate]
    rich_list = [x for x in rich_list if x not in duplicate]
    is_changed = True
    while(is_changed):
        is_changed = False
        for rich in rich_list[:]:
            left_team = get_left_idx(rich)
            right_team = get_right_idx(rich, N)

            if left_team in poor_list:
                rich_list.remove(rich)
                poor_list.remove(left_team)
                is_changed = True
            elif right_team in poor_list:
                rich_list.remove(rich)
                poor_list.remove(right_team)
                is_changed = True
    return len(poor_list)


if __name__ == '__main__':
    N, S, R = map(int, input().split())
    poor_list = list(map(int, input().split()))
    rich_list = list(map(int, input().split()))
    result = solution(N, poor_list, rich_list)
    print(result)
