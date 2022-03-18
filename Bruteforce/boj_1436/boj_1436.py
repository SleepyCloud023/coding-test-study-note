# https://www.acmicpc.net/problem/1436
# title: 영화감독 숌
# start: 2022-03-19 12:15:19 AM
# end:   2022-03-19 12:47:19 AM


def get_number(N: int):
    number = 666
    count = 1
    while (count < N):
        number += 1
        number_string = str(number)
        if number_string.find('666') != -1:
            count += 1
    return number


if __name__ == '__main__':
    N = int(input())
    result = get_number(N)
    print(result)
