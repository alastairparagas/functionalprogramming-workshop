/**
* Bad Example
*/

function mutatesParams(mutableObjectParam) {
  mutableObjectParam.newAddedProperty = "someValue";
  return mutableObjectParam;
}

var someObject = {
  key: "value"
};

var returnValue1 = mutatesParams(someObject);
console.log('newAddedProperty' in someObject);
console.log('newAddedProperty' in returnValue1);
console.log(someObject === returnValue1);



/**
* Good Example
*/

function doesNotMutateParams(mutableObjectParam) {
  var returnedObject = Object.assign({}, mutableObjectParam);
  
  returnedObject.newAddedProperty = "someValue";
  return returnedObject;
}

var someOtherObject = {
  key: "value"
};

var returnValue2 = doesNotMutateParams(someOtherObject);
console.log('newAddedProperty' in someOtherObject);
console.log('newAddedProperty' in returnValue2);
console.log(someOtherObject === returnValue2);

