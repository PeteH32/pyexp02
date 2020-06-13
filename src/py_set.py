
# Given 2 sets of integers, M and N, print their symmetric difference in ascending
# order. The term symmetric difference indicates those values that exist in
# either M or N but do not exist in both

def getSymmDiff(ms, ns):
    symdiff = set()

    for c in ms:
        if c not in ns:
            symdiff.add(c)
    for c in ns:
        if c not in ms:
            symdiff.add(c)

    # Can't sort set, so convert to list
    symdiff2 = list(symdiff)
    symdiff2.sort()

    return symdiff2

ms = [5, 4, 4, 2, 9]
ns = [2, 12, 4, 11, 12]
rc = getSymmDiff(ms, ns)
# 5
# 9
# 11
# 12
for c in rc:
    print(c)
