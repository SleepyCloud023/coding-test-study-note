# https://www.acmicpc.net/problem/5397
# 키로거

from collections import deque

# 5:18
# 6:00 => 42분


def solution(inputs: str) -> str:
    left = deque([])
    right = deque([])

    for char in inputs:
        if char == '<':
            if left:
                right.appendleft(left.pop())
        elif char == '>':
            if right:
                left.append(right.popleft())
        elif char == '-':
            if left:
                left.pop()
        else:
            left.append(char)

    return ''.join(left + right)


if __name__ == '__main__':
    N = int(input())
    result = [input() for _ in range(N)]
    result = map(solution, result)
    print(*result, sep='\n')
