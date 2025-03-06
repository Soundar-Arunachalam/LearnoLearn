import express from 'express';
import mongoose from 'mongoose';
import User from "./models/User.js"
import session from 'express-session';
import cors from 'cors';
import bodyParser from "body-parser";
const app =express();
const PORT=3000;
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cors());
app.use(express.json());
const DB="mongodb+srv://soundararunachalam3639:soundar@vijay.0vhdqhl.mongodb.net/?retryWrites=true&w=majority&appName=vijay"
app.use(
    session({
      secret: 'soundar', // Replace with a secure key
      resave: false,
      saveUninitialized: true,
      cookie: { secure: false }, // Use `true` for HTTPS
    })
  );
main();
async function main() {
    try{
  await mongoose.connect(DB);
  console.log("Db connection successfull");
await User.collection.dropIndex('certifications_1');
    }
    catch(err){
    console.log(err);
    }
}


app.post('/addstudent', async (req,res) => {
    const data = req.body;
    const user = new User(data);
    console.log(data);
    try {
        await user.save();
        console.log('hi');
        res.status(201).json(user);

    } catch (err) {
        res.status(400).json({ error: err.message });
    }
});


app.post('/login', async (req, res) => {
    try {
      
    const { id, password } = req.query;
      // Find the student by ID and password
      const student = await User.findOne({ id, password });
  
      if (!student) {
        return res.status(401).json({ message: 'Invalid credentials' });
      }
  
      // Create a session for the user
      req.session.student = {
        id: student.id,
        name: student.name,
      };
  
      return res.status(200).json({ message: 'Login successful', student: req.session.student });
    } catch (error) {
      console.error('Error during login:', error);
      return res.status(500).json({ message: 'An error occurred', error: error.message });
    }
  });



app.get('/getstudentdetails/:id', async (req,res) => {
    try {
        const studentId = req.params.id; // Extract the student ID from the route parameter
    
        // Find the student by ID
        const student = await User.findOne({ id: studentId});
    
        if (!student) {
          // If no student found, send a 404 response
          return res.status(404).json({ message: 'Student not found' });
        }
    
        // Return the student data
        return res.status(200).json(student);
      } catch (error) {
        console.error('Error fetching student details:', error);
    
        // Handle invalid IDs or other errors
        return res.status(500).json({ message: 'An error occurred', error: error.message });
      }
    
});

app.put('/updateStudent/:id', async (req, res) => {
    try {
      const { id } = req.params; // Student's unique ID
      const updates = req.body; // Fields to update
  
      // Find the student by ID and update their details
      const updatedStudent = await User.findOneAndUpdate(
        { id }, // Match by student ID
        updates, // Fields to update
        { new: true, runValidators: true } // Return the updated document and validate
      );
  
      if (!updatedStudent) {
        return res.status(404).json({ message: 'Student not found' });
      }
  
      return res.status(200).json({ message: 'Student updated successfully', student: updatedStudent });
    } catch (error) {
      console.error('Error updating student:', error);
      return res.status(500).json({ message: 'An error occurred', error: error.message });
    }
  });

app.listen(PORT,()=>{

    console.log(`app is running on port ${PORT}`);
})