# https://www.acmicpc.net/problem/2891
# 카약과 강풍

import sys
input = sys.stdin.readline


def get_left_team(idx: int):
    return max(0, idx-1)


def get_right_team(idx: int, N: int):
    return min(N, idx+1)


def solution(N: int, poor_set: set, rich_set: set):
    duplicate = set(poor_set) & set(rich_set)
    poor_set = poor_set - duplicate
    rich_set = rich_set - duplicate
    for team in range(1, N+1):
        if team in rich_set:
            left_team = get_left_team(team)
            right_team = get_right_team(team, N)
            if left_team in poor_set:
                poor_set.remove(left_team)
                rich_set.remove(team)
            elif right_team in poor_set:
                poor_set.remove(right_team)
                rich_set.remove(team)
    return len(poor_set)


if __name__ == '__main__':
    N, S, R = map(int, input().split())
    poor_set = set(map(int, input().split()))
    rich_set = set(map(int, input().split()))
    result = solution(N, poor_set, rich_set)
    print(result)
