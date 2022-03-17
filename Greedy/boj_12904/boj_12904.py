# https://www.acmicpc.net/problem/12904
# A와 B
# 3:55 start
# 4:11 end => 16분


def solution(S: str, T: str) -> int:
    num_cut = len(T) - len(S)
    list_T = list(T)

    while(num_cut > 0):
        last_char = list_T.pop()
        num_cut -= 1
        if last_char == 'B':
            list_T.reverse()

    result_T = ''.join(list_T)
    return 1 if result_T == S else 0


if __name__ == '__main__':
    S = input()
    T = input()
    result = solution(S, T)
    print(result)
