from functools import reduce

def reducer1(current, accumulated):
  return current * accumulated
results1 = reduce(reducer1, [1, 1, 3, 4, 5]);

def reducer2(current, accumulated):
  return current + accumulated
results2 = reduce(reducer2, ["ca", "fa", "ma", "ra"]);

print(results1);
print(results2);

