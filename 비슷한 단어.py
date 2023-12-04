import sys

input = lambda: sys.stdin.readline()

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def solution(words):
  result = 0

  base_word = words[0]
  base_dict = {char: 0 for char in ALPHA}
  for char in base_word:
    base_dict[char] += 1

  words_without_base = words[1:]
  for word in words_without_base:
    word_dict = {char: 0 for char in ALPHA}
    for char in word:
      word_dict[char] += 1

    total_gap = 0
    for char in ALPHA:
      gap = base_dict[char] - word_dict[char]
      if gap == 0:
        continue
      elif total_gap == 0 and (gap == 1 or gap == -1):
        total_gap = gap
        continue
      elif (gap == 1 and total_gap == -1) or (gap == -1 and total_gap == 1):
        gap = 100
        continue
      else:
        total_gap = -100
        break
    
    if total_gap != -100:
      result += 1

  return result

N = int(input())
WORDS = [input().strip() for _ in range(N)]
print(solution(WORDS))