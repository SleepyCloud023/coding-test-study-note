# https://www.acmicpc.net/problem/5585
# 거스름돈


def solution(N):
    result = 0
    remain = 1000 - N
    radix_list = [500, 100, 50, 10, 5, 1]
    for radix in radix_list:
        num_radix, remain = divmod(remain, radix)
        result += num_radix
        if remain == 0:
            break
    return result


if __name__ == "__main__":
    N = int(input())
    print(solution(N))
