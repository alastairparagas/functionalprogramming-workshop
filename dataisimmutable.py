# Bad Example

def mutatesParams(mutableObjectParam):
  mutableObjectParam["newAddedProperty"] = "someValue"
  return mutableObjectParam

someObject = {
  "key": "value"
}

returnValue1 = mutatesParams(someObject)
print("newAddedProperty" in someObject.keys())
print("newAddedProperty" in someObject.keys())
print(someObject == returnValue1)



# Good Example

import copy
   
def doesNotMutateParams(mutableObjectParam):
  returnedObject = copy.deepcopy(mutableObjectParam)
  
  returnedObject["newAddedProperty"] = "someValue"
  return returnedObject

someOtherObject = {
  "key": "value"
}

returnValue2 = doesNotMutateParams(someOtherObject);
print("newAddedProperty" in someOtherObject.keys())
print("newAddedProperty" in returnValue2.keys())
print(someOtherObject == returnValue2)

