// basic import that we are listening on
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const fs = require('fs');
const path = require('path');


const app = express();

//Getting server port
const PORT = process.env.PORT || 3000;


// Setup middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cors());

//checking exitance of data.json
const dataPath = path.join(__dirname, 'data.json');

if (!fs.existsSync(dataPath)) {
  fs.writeFileSync(dataPath, '[]');
}

// GET Method
app.get('/', function(req, res) {
  
});

// POST Method
app.post('/api/data', (req, res) => {
  const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
  data.push(req.body);
  fs.writeFileSync(dataPath, JSON.stringify(data));
  res.json(data);
});


// This can accept information, give back some, and do whatever!
app.all('/api/change-information', (req, res) => {
  
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

