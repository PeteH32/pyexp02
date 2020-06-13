#!/bin/python3

import math
import os
import random
import re
import sys

# Sherlock and Anagrams
#   https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Also see:
#   src/HackerRank/sherlock-and-anagrams-testcases/sherlock-and-anagrams-English.pdf
# NOTE: This implementation is much more performant. Took 1 sec with input03.txt
#   - it is still O(n**3)
#   - it's improvement is that some heavy work (getListOfPosCounts()) is only done once and then saved
#       - getListOfPosCounts() is the part that is still O(n**3)
#           - getListOfPosCounts() calls getLetterCounts()

def getLetterCounts(s):
    counts = {}     # dict: k,v = c,nCnt
    for ch in s:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] = counts[ch] + 1
    return counts

def areTheseAnagrams(s1, s2):
    if (len(s1) != len(s2)):
        return False
    cnts_s1 = getLetterCounts(s1)
    cnts_s2 = getLetterCounts(s2)
    for ch,nCnt in cnts_s1.items():
        if ch not in cnts_s2:
            return False
        if nCnt != cnts_s2[ch]:
            return False
    return True

# print(areTheseAnagrams("abba", "baba"), file=sys.stderr)
# print(areTheseAnagrams("abba", "baaa"), file=sys.stderr)
# print(areTheseAnagrams("abcba", "bacba"), file=sys.stderr)

def getListOfPosCounts(s):
    s_pos_counts = []   # [p0, p1,... pM] where pX is cnts = {ch: cnt}, 
                        # where pX=0...M=range(len(s))
    # for each posA in s
    #   // w = from pA to pB
    #   for each pB from pA to pM (len=1 then pA==pB)
    #       // get letter counts on w = posA+len
    #       s_pos_counts[p] = getLetterCounts
    for pA in range(len(s)):
        # pX's list of cnts for various lengths of w
        cnts_for_pA = []
        for pB in range(pA, len(s)):
            w = s[pA:(pB + 1)]
            cnts_for_w = getLetterCounts(w)
            cnts_for_pA.append(getLetterCounts(w))
        s_pos_counts.append(cnts_for_pA)
    return s_pos_counts

# print(getListOfPosCounts("abba"), file=sys.stderr)
# print(getListOfPosCounts("baba"), file=sys.stderr)
# print(getListOfPosCounts("bcabcac"), file=sys.stderr)

def areTheseCountsAnagrams(cnts1, cnts2):
    # cntsP = {k,v} = ch,nCnt
    if (len(cnts1) != len(cnts2)):
        return False
    cnts_s1 = cnts1
    cnts_s2 = cnts2
    for ch,nCnt in cnts_s1.items():
        if ch not in cnts_s2:
            return False
        if nCnt != cnts_s2[ch]:
            return False
    return True

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    n_total_anagrams = 0

    # // For each pos, get letter counts for all lens
    # // s_pos_counts = list of lists of dicts
    # [ [{'a': 1}, {'a': 1, 'b': 1}, {'a': 1, 'b': 2}, {'a': 2, 'b': 2}], 
    #   [{'b': 1}, {'b': 2}, {'b': 2, 'a': 1}], 
    #   [{'b': 1}, {'b': 1, 'a': 1}], 
    #   [{'a': 1}]]
    s_pos_counts_per_len = []   # [p] = cnts, p=range(len(s))
    s_pos_counts_per_len = getListOfPosCounts(s)

    # // For each pos, compare letterCounts
    # for each pos1 in s
    #   for each pos2 from pos1+1 to M
    #       // compare cnts[pos1] to cnts[pos2]
    #       if (areTheseCountsAnagrams(cnts1, cnts2))
    #           n_total_anagrams++
    for pw1 in range(len(s)):
        pw1_cnts = s_pos_counts_per_len[pw1]
        # print("PW1:", pw1_cnts)
        for pw2 in range((pw1+1),len(s)):
            pw2_cnts = s_pos_counts_per_len[pw2]
            # print("PW2:", pw2_cnts)
            for n in range(len(pw2_cnts)):
                if areTheseCountsAnagrams(pw1_cnts[n], pw2_cnts[n]):
                    n_total_anagrams = n_total_anagrams + 1

    return n_total_anagrams
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        # fptr.write(str(result) + '\n')
        print(result)

    # fptr.close()
