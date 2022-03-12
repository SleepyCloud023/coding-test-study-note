# https://www.acmicpc.net/problem/1459
# 걷기
import sys

input = sys.stdin.readline


def solution(x, y, w, s):
    result = 0
    x, y = max(x, y), min(x, y)
    if (s >= 2*w):
        result = w * (x+y)
    elif (w <= s < 2*w):
        result += s * y
        x, y = x-y, 0
        result += x * w
        x = 0
    elif (s < w):
        result += s * y
        x, y = x-y, 0
        result += 2 * s * (x // 2)
        x = x % 2
        result += w * x
        x = 0
    return result


if __name__ == '__main__':
    X, Y, W, S = map(int, input().split())
    result = solution(X, Y, W, S)
    print(result)
