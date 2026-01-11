const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.get('/user',(req, res)=>{
    res.json({message:'Returning list of users'});
});

app.post('/user',(req, res)=>{
    const newUser=req.body;
    res.json({message: 'User created', user: newUser});
});
app.put('/user/:id',(req, res)=>{
    const userId=req.params.id;
    const updateUser=req.body;
    res.json({ message: `User with ID ${userId} updated`, updatedUser});
});

app.delete('/user/:id',(req, res)=>{
    const userId=req.params.id;
    res.json({message:`user with ID ${userId} is deleted`});
});

app.patch('/user/:id',(req, res)=>{
    const userId=req.params.id;
    res.json({message:`user with id ${userId} is updated`})
});

app.listen(port,()=>{
    console.log('running')
});