var Evernote = require('evernote').Evernote;
var User = require('../models/User');
var Note = require('../models/Note');

exports.index = function(req, res) {
  var client = new Evernote.Client({token: req.user.oauth_token});
  var noteStore = client.getNoteStore();
  var guid = req.params.guid;
//  note =  noteStore.getNoteContent(guid,  function(err, note){
//  console.log(note); 
//});
  notetext = noteStore.getNoteContent(guid, function(err,notetext) {
     Note.findOne({guid:guid}, function(err,obj) { 
       obj.content_text = notetext;
       obj.save(function(err) {
         if (err) { 
           console.log(err);
         }
       }); 
console.log(notetext);
 res.render('note', { 


     title: obj.name,
     notetext: notetext,
   });
 });
});
};

