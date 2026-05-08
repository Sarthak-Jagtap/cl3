# -----------------------------
# FUZZY SET OPERATIONS
# -----------------------------

# Union of fuzzy sets
def fuzzy_union(A, B):
    result = {}

    for key in A:
        result[key] = max(A[key], B[key])

    return result


# Intersection of fuzzy sets
def fuzzy_intersection(A, B):
    result = {}

    for key in A:
        result[key] = min(A[key], B[key])

    return result


# Complement of fuzzy set
def fuzzy_complement(A):
    result = {}

    for key in A:
        result[key] = 1 - A[key]

    return result


# Difference of fuzzy sets (A - B)
def fuzzy_difference(A, B):
    result = {}

    for key in A:
        result[key] = min(A[key], 1 - B[key])

    return result


# -----------------------------
# CARTESIAN PRODUCT
# -----------------------------

def cartesian_product(A, B):
    relation = {}

    for a in A:
        for b in B:
            relation[(a, b)] = min(A[a], B[b])

    return relation


# -----------------------------
# MAX-MIN COMPOSITION
# -----------------------------

def max_min_composition(R, S, X, Y, Z):

    result = {}

    for x in X:
        for z in Z:

            values = []

            for y in Y:
                values.append(min(R[(x, y)], S[(y, z)]))

            result[(x, z)] = max(values)

    return result


# -----------------------------
# MAIN PROGRAM
# -----------------------------

# Fuzzy Set A
A = {
    'x1': 0.2,
    'x2': 0.7,
    'x3': 1.0
}

# Fuzzy Set B
B = {
    'x1': 0.5,
    'x2': 0.4,
    'x3': 0.8
}

print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)

# Union
print("\nUnion:")
print(fuzzy_union(A, B))

# Intersection
print("\nIntersection:")
print(fuzzy_intersection(A, B))

# Complement
print("\nComplement of A:")
print(fuzzy_complement(A))

# Difference
print("\nDifference (A - B):")
print(fuzzy_difference(A, B))


# -----------------------------
# FUZZY RELATIONS
# -----------------------------

X = ['x1', 'x2']
Y = ['y1', 'y2']
Z = ['z1', 'z2']

# Fuzzy Set P
P = {
    'x1': 0.7,
    'x2': 0.5
}

# Fuzzy Set Q
Q = {
    'y1': 0.6,
    'y2': 0.9
}

# Fuzzy Set R
R_set = {
    'z1': 0.8,
    'z2': 0.4
}

# Cartesian Products
R1 = cartesian_product(P, Q)
R2 = cartesian_product(Q, R_set)

print("\nFuzzy Relation R1:")
print(R1)

print("\nFuzzy Relation R2:")
print(R2)

# Max-Min Composition
composition = max_min_composition(R1, R2, X, Y, Z)

print("\nMax-Min Composition:")
print(composition)
