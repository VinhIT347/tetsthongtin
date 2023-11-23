const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));

// Simulate a simple in-memory database using JSON
const registrations = [];

app.post('/register', (req, res) => {
  const username = req.body.username;
  const email = req.body.email;

  // Save registration information to the "database"
  registrations.push({ username, email });

  console.log(`Đăng kí thành công! Username: ${username}, Email: ${email}`);
  res.send(`Đăng kí thành công! Username: ${username}, Email: ${email}`);
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
