N, K = map(int, input().split())
score = []
for i in range(N):
  n = map(int, input().split())
  score.append(sum(n))

sort_score = sorted(score, reverse=True)

for i in range(N):
  if sort_score[K-1] - score[i] <= 300:
    print('Yes')
  else:
    print('No')