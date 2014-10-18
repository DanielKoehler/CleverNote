var mongoose = require('mongoose/');


var NoteSchema = new mongoose.Schema({
  name: String,
  guid: String,
  notebook_guid: String,
  user_email: String,
  content_text: String,
  content_html: String,
});

var Note = mongoose.model('Note',NoteSchema);



