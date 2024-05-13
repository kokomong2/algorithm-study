import sys
import itertools



N, M = map(int, input().split())

for i in itertools.combinations_with_replacement(range(1, N+1), M):
    sys.stdout.write(' '.join(map(str, i)) + '\n')
