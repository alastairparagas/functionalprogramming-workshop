/**
* @param {int} initValue
* @param {Function} incrementEventListener - Function that fires
*   everytime the counter variable is incremented. Passed the 
*   new counter value
* @returns {Function} increments the closured counter variable
*/
function intIncrementer(initValue, incrementEventListener) {
  
  var counter = initValue;
  
  return function increment() {
    counter++;
    incrementEventListener(counter);
  }
  
}

const zeroIntIncrementer = intIncrementer(0, function (counterVal) {
  console.log("Counter value incremented - new value: " + counterVal);
});

zeroIntIncrementer();
zeroIntIncrementer();
zeroIntIncrementer();

