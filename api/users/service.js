const UserModel = require('./model');

const getAll = async () => {
    const users = UserModel.find({active: true});
    return users;
}

const getById = async (id) => {
    const user = await UserModel.find({_id: id, active: true});
    return user;
}

const getByHome = async (homeId) => {
    const users = await UserModel.find({home: homeId, active: true});
    return users;
}

const create = async (newUser) => {
    const user = new UserModel(newUser);
    try {
        await user.save();
    }
    catch(err) {
        console.error(err);
        return null;
    }
    return user;
}

const update = async (id, user) => {
    const result = await UserModel.findByIdAndUpdate(id, user);
    return result;
}

const remove = async (id) => {
    const result = await update(id, {active: false});
    return result;
}

module.exports = {
    getAll,
    getById,
    getByHome,

    create,

    update,

    remove,
};