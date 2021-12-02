const mongoose = require('mongoose');
require('dotenv').config();

const dbUri = process.env.DB_URI;

mongoose.connect(dbUri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

const db = mongoose.connection;
db.on('error', (er) => {
    console.error('MongoDB', er);
});
db.on('open', () => {
    console.info('MongoDB', 'connected');
});