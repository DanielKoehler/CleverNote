var Evernote = require('evernote').Evernote;
var User = require('../models/User');

exports.index = function(req, res) {
  var client = new Evernote.Client({token: req.user.oauth_token});
  var noteStore = client.getNoteStore();
  var guid = req.params.guid;
  note =  noteStore.getNoteContent(guid,  function(err, note) {
   res.render('note', { 
     title: 'Note',
     note: note,
   });
 });

};

