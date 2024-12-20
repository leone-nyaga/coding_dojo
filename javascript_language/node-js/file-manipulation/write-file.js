const fs = require('node:fs');

content = 'Asynchronous method to read and write from/into a file: To read/write the file in an asynchronous mode in the fs module we use the readFile() and writeFile() methods. The fs.readFile() takes three parameters first is the file name with the complete path, the second parameter takes the character encoding which is generally ‘utf-8’ and the third parameter is the callback function (which is fired after reading a complete file) with two parameters, one is the error in case error occurred while reading file and second is the data that we retrieve after reading the file and the fs.writeFile() also takes three parameters, file name with its complete path, the second parameter is the data to be written in file and the third is a callback function which fires in case an error occurs while writing the file.'

fs.writeFile('new-file.txt', content, err => {
  if (err) {
    console.error(err);
  } else {
    console.log('File written successfully!');
  }
});
