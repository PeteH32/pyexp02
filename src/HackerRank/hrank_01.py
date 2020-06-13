#!/bin/python3

import math
import os
import random
import re
import sys

# Hash Tables: Ransom Note
#   https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# See these files:
#   src/HackerRank/ctci-ransom-note-testcases/ctci-ransom-note-English.pdf
#   src/HackerRank/ctci-ransom-note-testcases

# Complete the checkMagazine function below.

def checkMagazine1(magazine, note):
    # NOTE: This is not performant, took too long with 30,000 words (16 sec on my machine)
    # The other checkMagazine uses dict (hashmap), and ran in <1 sec.
    for w in note:
        if w not in magazine:
            print("No")
            return
        magazine.remove(w)
    print("Yes")
    return

def getCounts(words):
    counts = {}     # k,v = word,count
    for w in words:
        if w not in counts:
            counts[w] = 1
        else:
            counts[w] = counts[w] + 1
    return counts

def checkMagazine(magazine, note):
    mcnts = getCounts(magazine)
    ncnts = getCounts(note)
    for w,cnt in ncnts.items():
        if w not in mcnts:
            print("No")
            return
        if mcnts[w] < cnt:
            print("No")
            return
    print("Yes")
    return


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    # Note: words are case-sensitive

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
