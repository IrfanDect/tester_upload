const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Alyssa Roberts;Tracy Woods;Pedro Gibson;Michelle Huff;Brenda Erickson;Anthony Banks;Jacob Murphy;Gabriel Oneill;Michelle Smith;');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
