const http = require('http');
const fs = require('fs');
const path = require('path');

const readStudentData = (databasePath) => {
    const data = fs.readFileSync(databasePath, 'utf-8');
    const lines = data.split('\n').filter(line => line.trim() !== '');
    
    let totalStudents = 0;
    const csStudents = [];
    const sweStudents = [];

    lines.forEach(line => {
        const [name, track] = line.split(',');
        if (track === 'CS') {
            csStudents.push(name);
        } else if (track === 'SWE') {
            sweStudents.push(name);
        }
        totalStudents++;
    });

    return {
        totalStudents,
        csStudents,
        sweStudents
    };
};

const app = http.createServer((req, res) => {
    const url = req.url;

    if (url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Hello Holberton School!\n');
    } else if (url === '/students') {
        const databasePath = process.argv[2];

        if (!databasePath) {
            res.writeHead(400, { 'Content-Type': 'text/plain' });
            res.end('Database file not provided\n');
            return;
        }

        const { totalStudents, csStudents, sweStudents } = readStudentData(databasePath);
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(`This is the list of our students\nNumber of students: ${totalStudents}\n` +
                `Number of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}\n` +
                `Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}\n`);
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found\n');
    }
});

const PORT = 1245;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

module.exports = app;
