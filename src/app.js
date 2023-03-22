const fs = require('fs');
import express from 'express';
import https from 'https'
import cors from 'cors';
import 'dotenv/config';

import { getTransactions } from './services/nubank'

const key = fs.readFileSync('./cert/CA/localhost/localhost.decrypted.key');
const cert = fs.readFileSync('./cert/CA/localhost/localhost.crt');
const app = express();

// Apply middlware for CORS and JSON endpoing
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.get('/transactions', async (req, res) => {
  console.log("run request")
  try {
    const transactions = await getTransactions()
    res.status(200).json(transactions)
  } catch (error) {
    res.status(400).json(error)
  }
})

const server = https.createServer({ key, cert }, app);

server.listen(process.env.PORT, () =>
  console.log(`listening on port ${process.env.PORT}!`),
);
