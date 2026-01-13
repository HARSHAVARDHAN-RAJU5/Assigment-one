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
    res.json({ message: `User with ID ${userId} updated`,
        updateUser:req.body
    });
});

app.patch('/user/:id',(req, res)=>{
    const userId=req.params.id;
    const update=req.body;
    res.json({message:`user with id ${userId} is updated`, update:req.body})
});

app.delete('/user/:id',(req, res)=>{
    const userId=req.params.id;
    res.json({message:`user with ID ${userId} is deleted`});
});


app.listen(port,()=>{
    console.log('running')
});