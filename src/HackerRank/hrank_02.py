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
# NOTE: This implementation was not performant enough. Took 11 sec with input03.txt

def get_letter_counts(w):
    cnts = {}   # k, v = c, cnt
    for c in w:
        if c not in cnts:
            cnts[c] = 1
        else:
            cnts[c] = cnts[c] + 1
    return cnts

def isAnagram(p1w, p2w):
    p1wCounts = get_letter_counts(p1w)
    p2wCounts = get_letter_counts(p2w)
    for c,cnt in p1wCounts.items():
        if c not in p2wCounts:
            return False
        if cnt != p2wCounts[c]:
            return False
    return True

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    # NOTE: This implementation was not performant enough. Took 11 sec with input03.txt
    # counter = 0
    # for each letter p1
    #   for each letter p2 after p1
    #       for each length of word starting at letter p1
    #           check anagram: p1 of len, p2 of same len
    #           if anagram, increment counter
    #  0123
    #  abba    ahhhhh  aabba
    #  12 L            01234
    num_anagrams = 0
    for p1 in range(len(s)):
        for p2 in range(p1 + 1, len(s)):
            for word_len in range(1, len(s) - p2 + 1):
                w1 = s[p1:(p1+word_len)]
                w2 = s[p2:(p2+word_len)]
                # print(p1, p2, word_len, ":", w1, w2)
                if isAnagram(w1, w2):
                    # print("words:", w1, "-", w2)
                    num_anagrams = num_anagrams + 1
    return num_anagrams

# print(isAnagram("abba", "bbaa"))
# print(isAnagram("abwba", "wbbaa"))
# print(isAnagram("abwba", "wbbaaa"))
# print(isAnagram("aabwba", "wbbaaa"))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        # fptr.write(str(result) + '\n')
        print(s, result)
        print()

    # fptr.close()
