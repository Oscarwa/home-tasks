const mongoose = require('mongoose'); // mongo db

const userSchema = new mongoose.Schema({
    firstName: {type: String},
    lastName: {type: String},
    email: {type: String, required: true, unique: true},
    imageUrl: {type: String},
    role: {type: String},
    home: {type: Number},
    active: {type: Boolean, default: true}
},
{
    versionKey: false,
});

const UserModel = new mongoose.model('users', userSchema);

module.exports = UserModel;
