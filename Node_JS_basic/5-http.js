// create complex HTTP server using http module
const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  const path = req.url.split('?')[0];
  if (path === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (path === '/students') {
    res.statusCode = 200;
    const databaseFile = process.argv[2];
    countStudents(databaseFile)
      .then((data) => {
        res.end(`This is the list of our students\n${data}`);
      })
      .catch((error) => {
        res.end(`This is the list of our students\n${error.message}`);
      });
  }
});

app.listen(1245);

module.exports = app;
