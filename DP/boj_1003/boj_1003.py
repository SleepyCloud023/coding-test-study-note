# https://www.acmicpc.net/problem/1003
# title: 피보나치 함수
# start: 2022-03-20 04:18:04 AM
# end:   2022-03-20 04:32:04 AM

import sys
input = sys.stdin.readline


def fibo(n):
    first = [1, 0]
    second = [0, 1]
    if n == 0:
        return first
    elif n == 1:
        return second

    n -= 1
    while(n > 0):
        next = [first[x] + second[x] for x in range(2)]
        first = second
        second = next
        n -= 1

    return next


if __name__ == '__main__':
    T = int(input())
    result = []
    for _ in range(T):
        n = int(input())
        result.append(fibo(n))

    for x in result:
        print(*x)
