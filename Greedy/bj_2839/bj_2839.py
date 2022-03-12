# 설탕배달
# https://www.acmicpc.net/problem/2839


def solution(N):
    num_3 = 0
    while(3 * num_3 <= N):
        current_left = N - 3 * num_3
        num_5, is_not_divided = divmod(current_left, 5)
        if(not is_not_divided):
            break
        num_3 += 1
    if is_not_divided:
        result = -1
    else:
        result = num_3 + num_5

    return result


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
