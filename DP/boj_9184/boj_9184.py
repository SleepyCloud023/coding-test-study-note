# https://www.acmicpc.net/problem/9184
# title: 신나는 함수 실행
# start: 2022-03-20 05:41:26 AM
# end:   2022-03-20 05:53:26 AM

dp = dict()


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        if (a, b, c) not in dp:
            dp[(a, b, c)] = w(20, 20, 20)

        return dp[(a, b, c)]

    elif a < b and b < c:
        if (a, b, c) not in dp:
            dp[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

        return dp[(a, b, c)]
    else:
        if (a, b, c) not in dp:
            dp[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + \
                w(a-1, b, c-1) - w(a-1, b-1, c-1)

        return dp[(a, b, c)]


if __name__ == '__main__':
    while(True):
        a, b, c = map(int, input().split())
        if (a, b, c) == (-1, -1, -1):
            break
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
