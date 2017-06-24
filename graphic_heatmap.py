import sys

maxscore, columns = next(sys.stdin).strip('\n').split('\t',1)

print(maxscore)
print(columns)
for line in sys.stdin:
	scores = line.strip('\n').split('\t')[1:]
	print(scores)
