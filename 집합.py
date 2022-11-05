import sys
input = sys.stdin.readline


def solution(instruction):
    if instruction[0] == "add":
        if int(instruction[1]) not in LIST:
            LIST.append(int(instruction[1]))

    elif instruction[0] == "remove":
        if int(instruction[1]) in LIST:
            LIST.remove(int(instruction[1]))

    elif instruction[0] == "check":
        if int(instruction[1]) in LIST:
            print("1")
        else:
            print("0")

    elif instruction[0] == "toggle":
        if int(instruction[1]) in LIST:
            LIST.remove(int(instruction[1]))
        else:
            LIST.append(int(instruction[1]))

    elif instruction[0] == "all":
        LIST.clear()
        for i in range(1, 21):
            LIST.append(i)

    elif instruction[0] == "empty":
        LIST.clear()


LIST = []

N = int(input())
for _ in range(N):
    INSTRUCTION = list(input().split())
    solution(INSTRUCTION)
