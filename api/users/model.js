const mongoose = require('mongoose'); // mongo db

const userSchema = new mongoose.Schema({
    firstName: {type: String},
    lastName: {type: String},
    imageUrl: {type: String},
    role: {type: String},
    home: {type: Number},
},
{
    versionKey: false,
});

const UserModel = new mongoose.model('users', userSchema);

module.exports = UserModel;
