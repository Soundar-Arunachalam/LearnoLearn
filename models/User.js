import mongoose from "mongoose";

const urlSchema = new mongoose.Schema({
  id: String,
  name: String,
  dept: String,
  password:{type: String, required: true},
  skillrackurl: {type: String},
  leetcodeurl: {type: String},
  githuburl:{type: String},
  researchpapers:{type: [String]},
  certifications:{type: [String]},
});
const User=mongoose.model('User', urlSchema);
 export default User;