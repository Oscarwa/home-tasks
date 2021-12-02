require('dotenv').config();
const express = require('express');
const morgan = require('morgan');

// DB
const db = require('./db');

// routes
const usersRoute = require('./users/routes');

const app = express();

app.use(morgan('dev'));
app.use(express.json());

app.use('/users', usersRoute);

app.get('/', (req, res, next) => {
    res.send('NazgulMX');
});


const port = process.env.PORT;
app.listen(port, () => {
    console.info(`App running on port: ${port}`);
});
