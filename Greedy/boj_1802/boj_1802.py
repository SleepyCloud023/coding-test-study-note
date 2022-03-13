# https://www.acmicpc.net/problem/1802
# 종이 접기

import sys
input = sys.stdin.readline


def check_yes(input_string: str) -> bool:
    if len(input_string) == 1:
        return True
    idx_center = len(input_string) // 2
    for i in range(1, idx_center+1):
        left = input_string[idx_center - i]
        right = input_string[idx_center + i]
        if left == right:
            return False

    return check_yes(input_string[:idx_center])


if __name__ == '__main__':
    N = int(input())
    string_list = []
    for _ in range(N):
        input_string = input().strip()
        string_list.append(input_string)

    result = ['YES' if check_yes(x) else 'NO' for x in string_list]
    print(*result, sep='\n')
