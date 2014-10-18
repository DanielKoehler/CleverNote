var Evernote = require('evernote').Evernote;
var User = require('../models/User');

exports.index = function(req, res) {
  var client = new Evernote.Client({token: req.user.oauth_token});
  var noteStore = client.getNoteStore();
  var noteFilter = new Evernote.NoteFilter;
  var guid = req.params.guid;
  noteFilter.notebookGuid = guid; 
  NoteList = new Evernote.NoteList;
 notes =  noteStore.findNotes(noteFilter, 0, 100,  function(err, notes) {
   console.log(notes);
   res.render('notes', { 
     title: 'Notes',
     notes: notes,
   });
 });

};

