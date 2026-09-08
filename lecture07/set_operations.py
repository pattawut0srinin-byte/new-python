set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))

print(set1.intersection(set2))

print(set1.difference(set2))

print(set1.symmetric_difference(set2))


set3 = {1,2,3,4}
set4 = {3,4,5,6}

union_set = set3 | set4
print("Union:", union_set)

intersection_set = set3 & set4
print("Intersection:", intersection_set)

difference_set = set3 - set4
print("Difference:", difference_set)

sym_diff_set = set3 ^ set4
print("Symmetric Difference:", sym_diff_set)