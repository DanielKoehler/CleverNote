var mongoose = require('mongoose');

var NotebookSchema = new mongoose.Schema({
  name: String,
  guid: {type:String,unique:true},
  user_email: String
});


var Notebook = mongoose.model('Notebook',NotebookSchema);

module.exports = mongoose.model('Notebook', NotebookSchema);

