# Sequence Types — list, tuple, range
#   - list
#   - tuple
#   - range

# list
print()
sq = [3,6,4,5]
for i in sq:
    print(i)

print()
sq = [ 
    [3,6], 
    [4,5,9], 
    [12,5,78]
]
for i in sq:
    print(i)

print()
for i in sq:
    for j in i:
        print(f"{j}, ", end="")
    print()

print(f"\nQUOTES:")
update = [
    ["DELL", "NASDAQ", 1045, 1118],
    ["DELL", "BATS", 1095, 1146],
    ["IBM", "NASDAQ", 1032, 1093],
    ["IBM", "BATS", 1092, 1160],
]
for q in update:
    print(q)
print("QUOTES again")
for i in range(len(update)):
    print(update[i])


# Set Types — set, frozenset
#   - set

# Mapping Types — dict
#   - dict

print("\n#### Dictionaries ####")
cnts = {'a':3, 'd':2, 'w':1, 's':7}
print(cnts)
for k,v in cnts.items():
    print(k,v)


print()
n = 13
r = range(1, n+1)
l = list(r)
print(f"n={n}, r={r}, l={l}")

print()
n = 3
for i in range(n):
    a, b = "4" "6"
    print (int(a) + int(b))

print()
