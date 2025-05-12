# GreedySorting

# Description
GreedySorting is a Python implementation of the greedy sorting algorithm for signed permutations. It transforms any signed permutation into the identity permutation by iteratively applying reversal operations. This approach is fundamental in computational biology and comparative genomics for studying genome rearrangements.

The algorithm corrects elements one by one: if an element is out of place, a signed reversal is applied to bring it (and its sign) into the correct position. Each transformation step is stored and returned.

# Features
* Transforms signed permutations into the identity permutation using a greedy approach.
* Tracks and returns each intermediate permutation step.
* Handles permutations with both positive and negative signs.
* Useful for understanding genome rearrangement distance.


 #  Function

```
 greedySorting(P)
```
# Purpose:
* Sorts a signed permutation into the identity permutation using a minimal number of signed reversals.

Parameters:

* P (list[int]): A list representing a signed permutation (e.g., [-3, 4, 1, 5, -2])

# Returns:

* list[list[int]]: A list of permutations representing each intermediate step in the greedy sorting process.


# Example
```
P = [-3, 4, 1, 5, -2]
result = greedySorting(P)

for perm in result:
    print(" ".join(map(str, perm)))
```
# Output:

3 4 1 5 -2
3 -4 1 5 -2
3 -4 -1 5 -2
3 -4 -1 -5 -2
3 -4 -1 -5 2


# Applications
* Comparative Genomics: Understanding genome rearrangement operations.
* Algorithm Education: Teaching sorting strategies for signed permutations.
* Bioinformatics Research: Modeling genome evolution through inversion distance.

# Requirements
*  Python 3.x
* No external libraries required

# License
* This project is licensed under the MIT License. See the LICENSE file for details.





