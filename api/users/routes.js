const express = require('express');
const router = express.Router();
const userService = require('./service'); 

router.get('/', async (req, res, next) => {
    const users = await userService.getAll();
    res.status(200).json({message: 'users!', data: users});
    next();
});

module.exports = router;