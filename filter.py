results1 = filter(lambda x: len(x) > 3, ["empire", "test", "cat", "ghost"])

results2 = filter(lambda x: x > 3, [1, 1, 5, 7, 8, 9, 1, 5])

print(list(results1));
print(list(results2));
