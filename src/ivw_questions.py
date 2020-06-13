
########################################
# Palindromes

def is_palindrome1(str):
    # NOTE: Won't work if str has spaces
    i = 0
    j = len(str) - 1
    while i < len(str):
        ci = str[i]
        cj = str[j]
        # print(i, ",", j, ": ", ci, " - ", cj)
        if ci != cj:
            return False

        i = i + 1
        j = j - 1

    return True

def is_palindrome3(str):
    str2 = str.replace(" ", "")
    return is_palindrome1(str2)

def test_palindrome(str):
    print(str, "= ", is_palindrome3(str))

print("\nPalindromes:")
test_palindrome("anna")
test_palindrome("asd")
test_palindrome("nursesrun")
test_palindrome("nurses run")

########################################
# Anagrams

def getLetterCounts(str):
    counts = {}    # {"a": 1, "f": 5}
    for c in str:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] = counts[c] + 1 
    return counts

# print("Letter counts:")
# print(getLetterCounts("inthecapitalsgrass"))

def compareCounts(cnts1, cnts2):
    for ltr,cnt in cnts1.items():
        if ltr not in cnts2:
            return False
        if cnts2[ltr] != cnt:
            return False
    return True

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    counts1 = getLetterCounts(s1)
    counts2 = getLetterCounts(s2)

    return compareCounts(counts1, counts2)

def test_anagram(s1, s2):
    print(s1, s2, "= ", is_anagram(s1, s2))

print("\nAnagrams:")
test_anagram("abba", "baba")
test_anagram("abba", "bab")
test_anagram("abbaa", "baaba")
test_anagram("abba", "baaa")

