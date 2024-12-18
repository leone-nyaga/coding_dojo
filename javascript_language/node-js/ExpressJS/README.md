# EXPRESS JS

ExpressJS is a web application framework that provides you with a simple API to build websites, web apps and back ends.

## How to install

You should have node js and npm installed and to check if they are installed run:
```bash
node -v
npm -v
```

Create a directory for your project and initialize it with:
```javascript
npm init -y
```
This will generate a ```package.json``` file.

Next install express with:
```javascript
npm install express
```
This will add Express as a dependency in your project.

Install ```nodemon``` in your project. nodemon is a tool that helps develop Node.js based applications by automatically restarting the node application when file changes in the directory are detected.
```javascript
 npm install --save-dev nodemon
```
This will install directly in the dev section in the ```package.json``` file.

## HELLO WORLD

```javascript
const express = require('express'); /* common method of importing express module in a file */
const app = express(); /* creates and returns an Express application instance, stored in the app variable */

/**
 * '/hello' is the route of the website http://localhost:5000
 * req: request represents incoming HTTP requests
 * res: response is the outgoing HTTP response used to send data back to the client
/
app.get('/hello', (req, res) => {
  res.send('HELLO WORLD'); /* send() is a method on the res object that sends the response body */
});

app.listen(5000);
``` 
