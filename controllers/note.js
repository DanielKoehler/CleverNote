var Evernote = require('evernote').Evernote;
var User = require('../models/User');
var Note = require('../models/Note');

exports.index = function(req, res) {
  var client = new Evernote.Client({token: req.user.oauth_token});
  var noteStore = client.getNoteStore();
  var guid = req.params.guid;
 // note =  noteStore.getNoteContent(guid,  function(err, note){
  // console.log(note); 
//});
  notetext = noteStore.getNoteSearchText(guid, 1,0, function(err,notetext) {
 res.render('note', { 
     title: 'Note',
     note: notetext,
   });
 });

};

