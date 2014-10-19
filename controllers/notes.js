var Evernote = require('evernote').Evernote;
var User = require('../models/User');
var Note = require('../models/Note');
exports.index = function(req, res) {
  var client = new Evernote.Client({token: req.user.oauth_token});
  var noteStore = client.getNoteStore();
  var noteFilter = new Evernote.NoteFilter;
  var guid = req.params.guid;
  noteFilter.notebookGuid = guid; 
  NoteList = new Evernote.NoteList;
  notes =  noteStore.findNotes(noteFilter, 0, 100,  function(err, notes) {
 var notes1 = notes.notes;
 for (var i in notes1) {
      var note = new Note({
        name: notes.notes[i].title,
        user_email: req.user.email,
        guid: notes.notes[i].guid,
        notebook_guid: notes.notes[i].notebookGuid,
   
      });
      note.save(function(err){
         if (err){console.log(err); } 
      });
 } 
    res.render('notes', { 
     title: 'Notes',
     notes: notes,
   });
 });

};

