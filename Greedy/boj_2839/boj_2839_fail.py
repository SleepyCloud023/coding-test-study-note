# 설탕배달
# https://www.acmicpc.net/problem/2839


def solution(N):
    coef_15, remain = divmod(N, 15)
    num_3 = 0
    while(3 * num_3 <= remain):
        current_left = remain - 3 * num_3
        num_5, is_not_divided = divmod(current_left, 5)
        if(not is_not_divided):
            break
        num_3 += 1
    if is_not_divided:
        result = -1
    else:
        result = coef_15 * 3 + num_3 + num_5

    return result


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
