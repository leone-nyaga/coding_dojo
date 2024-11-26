const fs = require('node:fs');

const content = 'Note: An Asynchronous method first completes the task (reading the file) and then fires the callback function.'

fs.writeFile('new-file.txt', content, { flag: 'a+' }, err => {
  if (err) {
    console.error(err);
  } else {
      console.log('Content appended successfully');
  }
});
