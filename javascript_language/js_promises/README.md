# PROMISES

A Promise is an object that represents a value that might not be available yet.

It’s a placeholder for a future result — either resolved or rejected.

Promises were introduced in JavaScript with ES6 in 2015.

A Promise is a JavaScript object used for managing asynchronous operations.

Promises allow you to write code that continues after a specific event occurs without blocking the execution of other code; JavaScript continues to read the code asynchronously.

Promises enable the handling of data that is not currently available but will be available in the future.

A Promise has three states in its structure, and when a Promise is initiated, it is in one of these three states:

+ Pending: This is the initial state when the Promise is neither fulfilled nor rejected. It represents the state of the Promise while the asynchronous operation is still ongoing.

+ Fulfilled: This state signifies that the asynchronous operation associated with the Promise has been successfully completed.

+ Rejected: This state indicates that the asynchronous operation has failed or been rejected for some reason.

When a Promise is either fulfilled or rejected, it enters the “settled” state, and in this step, there are two important methods:

+ then: When a Promise successfully transitions to the “fulfilled” state, the then method allows you to specify a callback function or code block that will work with the completed data. This is used to define what should happen when a successful result is obtained.

+ catch: When a Promise transitions to the “rejected” state, the catch method lets you specify a callback function or code block that will work with the rejected error. This is used to handle situations where the operation fails.
