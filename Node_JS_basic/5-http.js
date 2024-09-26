const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  const { url } = req;
  const message = async () => {
    await countStudents(process.argv[2]);
  };
  if (url === '/') res.end('Hello Holberton School!');
  else if (url === '/students') {
    try {
      const response = `This is the list of our students\n${message}`;
      res.end(response);
    } catch (err) {
      res.end(`${err.message}\n`);
    }
  }
});

app.listen(1245);

module.exports = app;
