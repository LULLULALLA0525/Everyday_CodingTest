import sys

input = lambda: sys.stdin.readline().rstrip()

def isAvailableIndex(board, index):
  for i in range(len(board)):
    if index == board[i]:
      return False
    elif abs(index - board[i]) == abs(len(board) - i):
      return False
  return True

def placeQueen(n, board):
  if len(board) == n:
    return 1
  
  count = 0
  for i in range(n):
    if isAvailableIndex(board, i):
      newBoard = board + [i]
      count += placeQueen(n, newBoard)

  return count

def solution(n):
  return placeQueen(n, [])

N = int(input())
print(solution(N))


# 더 빠른 코드, 하지만 복잡함
# def getAvailableIndexAfter(n, board):
#   inavailable = set()
#   for i in range(len(board)):
#     inavailable.add(board[i])
#     inavailable.add(board[i] - (len(board) - i))
#     inavailable.add(board[i] + (len(board) - i))

#   available = [i for i in range(n) if i not in inavailable]
#   return available

# def placeQueen(n, board):
#   if len(board) == n:
#     return 1
  
#   count = 0
#   available = getAvailableIndexAfter(n, board)
#   for i in available:
#     newBoard = board + [i]
#     count += placeQueen(n, newBoard)
  
#   return count

# def solution(n):
#   return placeQueen(n, [])

# N = int(input())
# print(solution(N))