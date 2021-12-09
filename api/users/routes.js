const express = require('express');
const router = express.Router();
const userService = require('./service'); 

router.get('/', async (req, res, next) => {
    const users = await userService.getAll();
    res.status(200).json({message: 'users!', data: users});
    next();
});
router.get('/:id', async (req, res, next) => {
    const user = await userService.getById(req.params.id);
    res.status(200).json({message: 'user!', data: user});
    next();
});
router.get('/home/:id', async (req, res, next) => {
    const user = await userService.getByHome(req.params.id);
    res.status(200).json({message: 'user!', data: user});
    next();
});


router.post('/', async (req, res, next) => {
    const user = await userService.create(req.body);
    if(user) {
        res.status(200).json({message: 'created!', data: user});
    } else {
        res.status(415).json({message: 'Error!', data: null, error: "Error creating user" });
    }
    next();
});

router.patch('/:id', async (req, res, next) => {
    const user = await userService.update(req.params.id, req.body);
    res.status(200).json({message: 'update!', data: user});
    next();
});

router.delete('/:id', async (req, res, next) => {
    const user = await userService.remove(req.params.id);
    res.status(200).json({message: 'deleted!', data: user});
    next();
});

module.exports = router;