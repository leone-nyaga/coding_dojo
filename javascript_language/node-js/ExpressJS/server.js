const express = require('express');
const app = express();

app.get('/hello', (req, res) => {
  res.send('HELLO WORLD');
});

app.listen(5000);
