# FILE MANIPULATION

Node. js provides the functionality to read and write files from the computer. Reading and Writing the file in Node. js is done by using one of the coolest Node. js modules called fs module, it is one of the most well-known built-in Node.

### Writing a file

The easiest way to write to files in Node.js is to use the fs.writeFile() API.

```node
const fs = require('node:fs');

const content = 'Some content!';

fs.writeFile('/Users/joe/test.txt', content, err => {
  if (err) {
    console.error(err);
  } else {
    // file written successfully
  }
});
```

### Writing a file synchronously

Alternatively, you can use the synchronous version fs.writeFileSync():

```node
const fs = require('node:fs');

const content = 'Some content!';

try {
  fs.writeFileSync('/Users/joe/test.txt', content);
  // file written successfully
} catch (err) {
  console.error(err);
}
```

You can modify the default by specifying a flag:
```node
fs.writeFile('/Users/joe/test.txt', content, { flag: 'a+' }, err => {});
```

The flags you'll likely use are:

