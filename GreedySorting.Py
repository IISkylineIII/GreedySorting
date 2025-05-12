def greedySorting(P):
    def apply_reversal(P, k):
        # Apply the k-sorting reversal to permutation P.
        return P[:k-1] + [-x for x in reversed(P[k-1:k])] + P[k:]

    n = len(P)
    permutations = []  # List to store the sequence of permutations

    for k in range(1, n + 1):
        if P[k - 1] != k:
            # If the element is not sorted, apply the k-sorting reversal
            P = apply_reversal(P, k)
            permutations.append(P.copy())  # Append a copy of the current state

        if P[k - 1] == -k:
            # If the element is -k, apply the k-sorting reversal again
            P = apply_reversal(P, k)
            permutations.append(P.copy())  # Append a copy of the current state

    return permutations

P = [-3, 4, 1, 5, -2]

result = greedySorting(P)

for perm in result:
    print(" ".join(map(str, perm)))
