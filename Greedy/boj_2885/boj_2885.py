# https://www.acmicpc.net/problem/2885
# 초콜릿 식사

# 5:46 start
# 6:20 pass => 34분


def solution(K: int):
    binary_choco = bin(K)[2:]
    min_choco = binary_choco.strip('0')
    big_choco_pow = len(binary_choco)
    min_count = len(min_choco)
    if len(min_choco) == 1:
        big_choco_pow -= 1
        min_count -= 1
    return (2 ** big_choco_pow, min_count)


if __name__ == '__main__':
    K = int(input())
    result = solution(K)
    print(*result)
