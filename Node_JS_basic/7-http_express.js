const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/students', async (req, res) => {
  try {
    const message = countStudents(process.argv[2]);
    const response = `This is the list of our students\n${message}`;
    res.end(response);
  } catch (err) {
    res.end(`${err.message}\n`);
  }
});

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
