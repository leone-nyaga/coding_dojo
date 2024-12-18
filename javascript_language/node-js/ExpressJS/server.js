const express = require('express');
const app = express();

app.set('view engine', 'ejs');

app.get('/hello', (req, res) => {
  res.send('HELLO WORLD');
});

app.get('/index1', (req, res) => {
  const name = 'Mike';
  res.render('index', {name});
});

app.listen((5000), () => {
  console.log('app listening on port 5000');
});
