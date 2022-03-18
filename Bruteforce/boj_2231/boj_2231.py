# https://www.acmicpc.net/problem/2231
# title: 분해합
# start: 2022-03-18 10:49:45 PM
# end:   2022-03-18 10:59:20 PM


def get_min_creator(N: int, length: int):
    min_number = max(1, N - 9 * length)

    # N-1 까지 체크
    for number in range(min_number, N):
        radix_list = list(map(int, str(number)))
        sum_radix = sum(radix_list)
        if number + sum_radix == N:
            return number

    return 0


if __name__ == '__main__':
    str_N = input()
    N = int(str_N)
    result = get_min_creator(N, len(str_N))
    print(result)
