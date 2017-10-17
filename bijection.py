from collections import Counter
import operator

def bijection_machine(partition, A, B):
    A = [Counter(x) for x in A]
    B = [Counter(x) for x in B]
    partition = Counter(partition)
    diseases = []
    while (True):
        # f() to convert diseases in A to diseases in B
        f_and_f_inverse(diseases, A, B, partition)
        # beta() to either add or remove smallest disease present
        alpha_and_beta(diseases, B, partition)
        # if there are no diseases listed after beta(), we know it is a fixed point
        if (not diseases): return sorted((+partition).elements())
        # f^-1() to convert diseases in B to diseases in A
        f_and_f_inverse(diseases, B, A, partition)
        # alpha() to either add or remove smallest disease present
        alpha_and_beta(diseases, A, partition)

def alpha_and_beta(diseases, diseaseList, partition):
    for i, disease in enumerate(diseaseList):
        if not (disease - partition) and i in diseases:
            diseases.remove(i)
            break
        elif not (disease - partition) and i not in diseases:
            diseases.append(i)
            break

def f_and_f_inverse(diseases, fromList, toList, partition):
    for disease in diseases:
        partition.subtract(fromList[disease])
        partition.update(toList[disease])

# USAGE: Enter 2 lists of diseases, A and B (should be lists of lists) and an integer partition (list of integers)
# Below is an example input for which the output should be the partition [4, 10]
# A = [[2], [3], [4], [6], [8], [9], [10]]
# B = [[1,1], [3], [2,2], [6], [4,4], [9], [5,5]]
# partition = [1, 1, 1, 1, 5, 5]
# print(bijection_machine(partition, A, B))