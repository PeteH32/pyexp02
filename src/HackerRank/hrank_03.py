#!/bin/python3

import math
import os
import random
import re
import sys

# Frequency Queries
#   https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D=dictionaries-hashmaps
# Also see:
#   src/HackerRank/frequency-queries-testcases
# NOTE: This implementation is not performant. Failed input11.txt

# Complete the freqQuery function below.
def freqQuery(queries):
    # queries: a 2-d array of integers, eg [[1,5],[1,6], [3,2]]
    counts_for_n = {}   # k,v = n, cnt
    answers = []
    for q in queries:
        cmd = q[0]
        n = q[1]
        if cmd == 1:
            # cnt++
            counts_for_n[n] = counts_for_n.get(n, 0) + 1
        elif cmd == 2:
            # cnt--, if now 0 then delete
            cnt = counts_for_n.get(n)
            if cnt is not None:
                if cnt == 1:
                    del counts_for_n[n]
                else:
                    counts_for_n[n] = counts_for_n[n] - 1
            else:
                # Nothing to do
                pass
        elif cmd == 3:
            # Check if any integer is present whose frequency is exactly n. If yes, print 1 else 0.
            answer = 0
            for k,v in counts_for_n.items():
                if v == n:
                    answer = 1
                    break
            answers.append(answer)
        # print(counts_for_n)
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
