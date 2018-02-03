"""
@param {int} initValue
@param {Function} incrementEventListener - Function that fires 
  everytime the counter variable is incremented. Passed the 
  new counter value
@returns {Function} increments the closured counter variable
"""
def intIncrementer(initValue, incrementEventListener):
  
  counter = initValue
  
  def increment():
    nonlocal counter
    counter = counter + 1
    incrementEventListener(counter)
  
  return increment
  
zeroIntIncrementer = intIncrementer(
  0, 
  lambda counter: print("Counter value incremented - new value: {counterVal}".format(
    counterVal=counter
  ))
)

zeroIntIncrementer()
zeroIntIncrementer()
zeroIntIncrementer()
