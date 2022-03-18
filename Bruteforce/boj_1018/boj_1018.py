# https://www.acmicpc.net/problem/1018
# title: 체스판 다시 칠하기
# start: 2022-03-18 11:46:24 PM
# end:   2022-03-19 00:06:00 PM


# 1: W, 0: B
def count(M: int, N: int, matrix: list):
    first = [1, 0] * 4
    second = [0, 1] * 4
    compare_list = [first, second]

    result = 1e9

    for i in range(M - 7):
        for j in range(N - 7):
            count_1 = 0
            count_2 = 0
            for m in range(8):
                cur_row = matrix[i+m]
                check_1 = compare_list[m % 2]
                check_2 = compare_list[(m+1) % 2]
                diff_1 = [1 if cur_row[j + x] != check_1[x]
                          else 0 for x in range(8)]
                diff_2 = [1 if cur_row[j + x] != check_2[x]
                          else 0 for x in range(8)]
                count_1 += sum(diff_1)
                count_2 += sum(diff_2)
            result = min(result, count_1, count_2)

    return result


if __name__ == '__main__':
    M, N = map(int, input().split())
    matrix = []
    for _ in range(M):
        row = [1 if char == 'W' else 0 for char in input()]
        matrix.append(row)
    result = count(M, N, matrix)
    print(result)
