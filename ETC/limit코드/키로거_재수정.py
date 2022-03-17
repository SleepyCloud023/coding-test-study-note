# 백준 | 키로거 : (https://www.acmicpc.net/problem/5397)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)


class Node:
    left = None
    right = None
    value = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        left = self.left.value if self.left is not None else "None"
        value = self.value
        right = self.right.value if self.right is not None else "None"
        return left + " " + value + " " + right


def solution(input):
    pointer = Node("")

    for i in input:
        if i == "<":
            prev_left = pointer.left
            if prev_left:
                prev_left.value, pointer.value = pointer.value, prev_left.value
                pointer = prev_left

        elif i == ">":
            prev_right = pointer.right
            if prev_right:
                pointer.value, prev_right.value = prev_right.value, pointer.value
                pointer = prev_right

        elif i == "-":
            prev_left = pointer.left
            if prev_left:
                prev_left.right = pointer.right
                prev_left.value = pointer.value
                pointer = prev_left

        else:
            new_node = Node(i)
            prev_left = pointer.left
            new_node.right = pointer
            pointer.left = new_node
            if prev_left:
                new_node.left = prev_left
                prev_left.right = new_node

    password_left = []
    password_right = []
    left_node = pointer.left
    right_node = pointer.right

    while(left_node):
        password_left.append(left_node.value)
        left_node = left_node.left

    while(right_node):
        password_right.append(right_node.value)
        right_node = right_node.right

    return ''.join(password_left[::-1]) + ''.join(password_right)


if __name__ == '__main__':
    n = int(input())
    result = []
    for i in range(n):
        result.append(input())
    result = [solution(x) for x in result]
    print(*result, sep='\n')
