results1 = map(lambda x: x + 1, [1, 2, 3, 4, 5, 6]);

results2 = map(lambda x: x + "t", ["ca", "fa", "ma", "ra"]);

results3 = map(lambda x: not x, [True, False]);

print(list(results1))
print(list(results2))
print(list(results3))

