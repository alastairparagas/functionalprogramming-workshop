var results1 = [1, 2, 3, 4, 5, 6].map(function (x) {
  return x++;
});

var results2 = ["ca", "fa", "ma", "ra"].map(function (x) {
  return x + "t";
});

var results3 = [true, false].map(function (x) {
  return !x;
});

console.log(results1);
console.log(results2);
console.log(results3);


