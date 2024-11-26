const fs = require('node:fs');

fs.open('file.txt', 'r', (err, fd) => {
  if (err) {
    console.error(err);
    return;
  }

