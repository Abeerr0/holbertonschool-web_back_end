// read file asynchronously and return a Promise
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // filter out empty lines
      const lines = data.split('\n').filter((line) => line.trim().length > 0);
      if (lines.length <= 1) {
        console.log('Number of students: 0');
        resolve('Number of students: 0');
        return;
      }

      const studentRows = lines.slice(1);
      const output = [];
      const totalMsg = `Number of students: ${studentRows.length}`;
      console.log(totalMsg);
      output.push(totalMsg);

      const fields = {};
      for (const row of studentRows) {
        const student = row.split(',');
        if (student.length >= 4) {
          const firstName = student[0].trim();
          const field = student[student.length - 1].trim();

          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstName);
        }
      }

      for (const [field, list] of Object.entries(fields)) {
        const fieldMsg = `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
        console.log(fieldMsg);
        output.push(fieldMsg);
      }

      resolve(output.join('\n'));
    });
  });
}

module.exports = countStudents;
