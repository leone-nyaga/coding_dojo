const fs = require('node:fs');

const content = 'Synchronous method to read the file: To read the file in the synchronous mode we use a method in the fs module which is readFileSync(). It takes two parameters first is the file name with a complete path and the second parameter is the character encoding which is generally ‘utf-8’.'

fs.appendFile('file.txt', content, err => {
  if (err) {
    console.error(err);
  } else {
    console.log('File appended successfully!');
  }
});
