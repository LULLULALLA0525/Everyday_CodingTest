
def solution(board, moves):
    answer = 0;

    basket = []
    for move in moves:
        move -= 1
        for i in range(len(board)):
            if board[i][move] != 0:
                picked_doll = board[i][move]
                board[i][move] = 0
                if len(basket) == 0:
                    basket.append(picked_doll)
                elif picked_doll == basket[-1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(picked_doll)
                break
        
    return answer

board = []
first_row = list(map(int, input().split()))
board.append(first_row)
for _ in range(len(first_row) - 1):
    board.append(list(map(int, input().split())))

moves = list(map(int, input().split()))

"""
0 0 0 0 0
0 0 1 0 3
0 2 5 0 1
4 2 4 4 2
3 5 1 3 1
1 5 3 5 1 2 1 4

4 3 1 1 3 2 0 4
"""

print(solution(board, moves))