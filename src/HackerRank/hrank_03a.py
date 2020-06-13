#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    # queries: a 2-d array of integers, eg [[1,5],[1,6], [3,2]]
    counts_for_n = {}   # k,v = n, cnt
    cnt_to_freq_map = {}       # k,v = cnt, freq
    answers = []
    for q in queries:
        cmd = q[0]
        n = q[1]
        if cmd == 1:
            # cnt++
            if n not in counts_for_n:
                counts_for_n[n] = 1
            else:
                counts_for_n[n] = counts_for_n[n] + 1
            # Increment this cnt's freq
            # TODO - THIS WON'T WORK. Need to incr(new-cnt) and decr(old-cnt)
            cnt_to_freq_map[1] = cnt_to_freq_map.get(1, 0) + 1
        elif cmd == 2:
            # cnt--, if now 0 then delete
            cnt = counts_for_n.get(n)
            if cnt is not None:
                if cnt == 1:
                    # We're deleting last occurrence of n, so remove from counts_for_n
                    del counts_for_n[n]
                else:
                    # There's >1 occurrences of n, so still track counts_for_n
                    counts_for_n[n] = counts_for_n[n] - 1
                    # Decrement this cnt's freq
                    # TODO - THIS WON'T WORK. Need to incr(new-cnt) and decr(old-cnt)
                    cnt_to_freq_map[1] = cnt_to_freq_map.get(1, 0) - 1
            else:
                # n is not in our counts_for_n, so nothing to delete
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
