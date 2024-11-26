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

|Flag	|Description					|File gets created if it doesn't exist|
|:------|:----------------------------------------------|:------------------------------------|
|'r+'   |This flag opens the file for reading and writing|	No			      |
|'w+'	|This flag opens the file for reading and writing and it also positions the stream at the beginning of the file|	Yes	|
|'a'	|This flag opens the file for writing and it also positions the stream at the end of the file|	Yes	|
|'a+'	|This flag opens the file for reading and writing and it also positions the stream at the end of the file|	Yes	|

### Appending content to a file

Appending to files is handy when you don't want to overwrite a file with new content, but rather add to it.
A handy method to append content to the end of a file is fs.appendFile() (and its fs.appendFileSync() counterpart):

```node
const fs = require('node:fs');

const content = 'Some content!';

fs.appendFile('file.log', content, err => {
  if (err) {
    console.error(err);
  } else {
    // done!
  }
});
```


