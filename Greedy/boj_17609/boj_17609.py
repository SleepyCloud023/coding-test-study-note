# https://www.acmicpc.net/problem/17609
# 회문(palindrome)
# 12:29 start
# 2:18 end

import sys
input = sys.stdin.readline


def is_palindrome(target: str):
    idx_center = len(target)//2

    if len(target) % 2 == 0:
        # abba
        return target[:idx_center][::-1] == target[idx_center:]
    else:
        # abcba
        return target[:idx_center][::-1] == target[idx_center + 1:]


# 회문: 0, 유사회문: 1, 그 외: 2
def solution(target: str):
    result = 0
    left_idx = 0
    right_idx = len(target) - 1

    while(left_idx < right_idx):
        left = target[left_idx]
        right = target[right_idx]
        if left == right:
            left_idx += 1
            right_idx -= 1
        else:
            remove_left = is_palindrome(target[left_idx+1: right_idx+1])
            remove_right = is_palindrome(target[left_idx: right_idx])
            if remove_left or remove_right:
                result = 1
            else:
                result = 2
            break
    return result


if __name__ == '__main__':
    result = []
    N = int(input())
    for _ in range(N):
        target = input().rstrip()
        result.append(solution(target))
    print(*result, sep='\n')
