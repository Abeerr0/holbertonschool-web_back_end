// read file synchronously
const fs = require('fs');

function countStudents(path) {
  let content;
  try {
    content = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  // filter out empty lines
  const lines = content.split('\n').filter((line) => line.trim().length > 0);
  if (lines.length <= 1) {
    console.log('Number of students: 0');
    return;
  }

  // ignore header line
  const studentRows = lines.slice(1);
  console.log(`Number of students: ${studentRows.length}`);

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
    console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
  }
}

module.exports = countStudents;
