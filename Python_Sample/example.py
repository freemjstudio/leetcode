import itertools

# permutation
a = ['A', 'B', 'C']
nPr = itertools.permutations(a,2)
print(list(nPr))

b = ['A', 'B', 'C']
nCr = itertools.combinations(b, 2)
print(list(nCr))