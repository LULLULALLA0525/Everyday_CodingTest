import sys

input = lambda: sys.stdin.readline()

def solution(m, words):
  note = dict()
  filtered_words = list(filter(lambda word: len(word) >= m, words))
  for word in filtered_words:
    if word in note:
      note[word] += 1
    else:
      note[word] = 1

  sorted_words = sorted(note.items(), key=lambda word, counts: (-counts, -len(word), word[0]))
  for word in sorted_words:
    print(word)

N, M = list(map(int, input().split()))
WORDS = [input().strip() for _ in range(N)]
solution(M, WORDS)