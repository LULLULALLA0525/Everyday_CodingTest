CHESS_BOARD_1 = [["W", "B", "W", "B", "W", "B", "W", "B"],
				["B", "W", "B", "W", "B", "W", "B", "W"],
				["W", "B", "W", "B", "W", "B", "W", "B"],
				["B", "W", "B", "W", "B", "W", "B", "W"],
				["W", "B", "W", "B", "W", "B", "W", "B"],
				["B", "W", "B", "W", "B", "W", "B", "W"],
				["W", "B", "W", "B", "W", "B", "W", "B"],
				["B", "W", "B", "W", "B", "W", "B", "W"]]

CHESS_BOARD_2 = [["B", "W", "B", "W", "B", "W", "B", "W"],
				["W", "B", "W", "B", "W", "B", "W", "B"],
				["B", "W", "B", "W", "B", "W", "B", "W"],
				["W", "B", "W", "B", "W", "B", "W", "B"],
				["B", "W", "B", "W", "B", "W", "B", "W"],
				["W", "B", "W", "B", "W", "B", "W", "B"],
				["B", "W", "B", "W", "B", "W", "B", "W"],
				["W", "B", "W", "B", "W", "B", "W", "B"]]

def cut(board, start_row, start_column):
	result = [[board[row][column] for column in range(start_column, start_column + 8)] for row in range(start_row, start_row + 8)]
	# for row in range(8):
	# 	print(''.join(result[row]))
	return result

def compare(board1, board2):
	cnt = 0
	for row in range(8):
		for column in range(8):
			if board1[row][column] != board2[row][column]:
				cnt += 1
	return cnt

def solution(board, r, c):
	answer = 65
	for start_row in range(r - 7):
		for start_column in range(c - 7):
			dif1 = compare(cut(board, start_row, start_column), CHESS_BOARD_1)
			if dif1 < answer:
				answer = dif1
			dif2 = compare(cut(board, start_row, start_column), CHESS_BOARD_2)
			if dif2 < answer:
				answer = dif2
	return answer

r, c = list(map(int, input().split()))
board = []
for _ in range(r):
	board.append(input())
	
print(solution(board, r, c))