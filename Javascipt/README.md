Day-1

```js
// We use const for things that don't change
const myGoal = "Become a JS Developer";

// We use let for things that might change
let currentLesson = 1;

// Print them to see the output
console.log(myGoal, currentLesson);
```


DATATYPES 
```js

//String: Text data
let name = "Gemini"; // Double quotes
let city = 'Delhi';  // Single quotes

//Number: Both integers and decimals (floats)
let age = 21;
let price = 99.99;

//Boolean: Logical entities. Only two values: true or false
let isStudent = true;
let isTired = false;

//Undefined: A variable that has been declared but not assigned a value yet
let score; // value is currently 'undefined'

//Null: Represents "intentional absence" of any object value. You set this manually to say "this is empty
let emptyBox = null;

//TypeOf Operator
console.log(typeof "Hello"); // Output: "string"
console.log(typeof 42);      // Output: "number"
console.log(typeof true);    // Output: "boolean"
```


Even though null is a Primitive type (as listed in your roadmap under "Primitive Types"), typeof null returns 'object'. This is a historical error in the language that can't be fixed now without breaking old websites. Just remember: logically, it is not an object.

