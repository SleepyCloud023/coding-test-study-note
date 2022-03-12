# https://www.acmicpc.net/problem/1543
# 문서검색

import sys
input = sys.stdin.readline


def solution(docs: str, word: str):
    next_idx = 0
    result = 0
    docs_length = len(docs)
    word_length = len(word)
    for i in range(docs_length + 1 - word_length):
        if i < next_idx:
            continue
        current_word = docs[i: i + word_length]
        if current_word == word:
            result += 1
            next_idx = i + word_length
    return result


if __name__ == "__main__":
    docs = input().strip()
    word = input().strip()
    result = solution(docs, word)
    print(result)
