n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

def modify(score):
	return score/max_score*100

modified_scores = list(map(modify, scores))
print(sum(modified_scores)/n)