var results1 = [1, 1, 3, 4, 5].reduce(function (current, accumulated) {
  return current * accumulated;
});

var results2 = ["ca", "fa", "ma", "ra"].reduce(function (current, accumulated) {
  return current + accumulated;
});

console.log(results1);
console.log(results2);

