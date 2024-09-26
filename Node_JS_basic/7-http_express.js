const http = require('http');
const fs = require('fs').promises;

async function countStudents(filepath) {
  try {
    const csv = await fs.readFile(filepath, { encoding: 'utf8' });
    const lines = csv.split(/\r?\n|\n/);
    const headers = lines[0].split(',');

    const dictList = lines.slice(1)
      .map(line => line.split(','))
      .filter(data => data.length === headers.length)
      .map(data => {
        const row = {};
        headers.forEach((header, index) => {
          row[header.trim()] = data[index].trim();
        });
        return row;
      });

    let countCS = 0;
    let countSWE = 0;
    const studentsCS = [];
    const studentsSWE = [];

    dictList.forEach(({ field, firstname }) => {
      if (field === 'CS') {
        countCS += 1;
        studentsCS.push(firstname);
      } else if (field === 'SWE') {
        countSWE += 1;
        studentsSWE.push(firstname);
      }
    });

    const totalStudents = countCS + countSWE;

    return {
      totalStudents,
      countCS,
      countSWE,
      studentsCS,
      studentsSWE,
    };
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

const pathToDB = process.argv[2];
const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const {
        totalStudents,
        countCS,
        countSWE,
        studentsCS,
        studentsSWE,
      } = await countStudents(pathToDB);

      res.write('This is the list of our students\n');
      res.write(`Number of students: ${totalStudents}\n`);
      res.write(`Number of students in CS: ${countCS}. List: ${studentsCS.join(', ')}\n`);
      res.write(`Number of students in SWE: ${countSWE}. List: ${studentsSWE.join(', ')}`);
      res.end();
    } catch (error) {
      res.statusCode = 500;
      res.end('Error: Cannot load the database');
    }
  } else {
    res.statusCode = 404;
    res.end('Error: Not Found');
  }
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
