const UserModel = require('./model');

const getAll = async () => {
    const users = UserModel.find({});
    return users;
}

module.exports = {
    getAll
};