# https://www.acmicpc.net/problem/12865
# title: 평범한 배낭
# start: 2022-03-21 08:45:46 AM
# end:   2022-03-21 09:10:46 AM

def solution(N, K, bag_list: list):
    # 0...N-1
    # bag_list : [(Weight, Value) ...]
    # 0...N
    # 무게가 0일때 N번째 가방으로 만들 수 있는 가장 큰 가치
    dp = [0] * (K+1)

    for idx_bag in range(1, N+1):
        cur_bag = bag_list[idx_bag-1]
        # 이전 상태의 dp[weight - cur_bag[0]]를 참조해야 하므로
        # iterator는 큰 무게에서부터 시작해야함
        for weight in range(K, 0, -1):
            if cur_bag[0] <= weight:
                # 이번 가방 X VS 이번 가방 O
                not_choose = dp[weight]
                choose = dp[weight - cur_bag[0]] + cur_bag[1]
                dp[weight] = max(not_choose, choose)

    return dp[K]


if __name__ == '__main__':
    N, K = map(int, input().split())
    bag_list = []
    for _ in range(N):
        bag = tuple(map(int, input().split()))
        bag_list.append(bag)
    result = solution(N, K, bag_list)
    print(result)
