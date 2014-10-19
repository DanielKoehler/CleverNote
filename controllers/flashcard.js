var Evernote = require('evernote').Evernote;
var User = require('../models/User');
var Note = require('../models/Note');
var PythonShell = require('python-shell'); 
var JSON = require('json');

exports.index = function(req, res) {
  var client = new Evernote.Client({token: req.user.oauth_token});
  var noteStore = client.getNoteStore();
  var guid = req.params.guid;
  notetext = noteStore.getNoteSearchText(guid, 1, 0,function(err,notetext) {
     Note.findOne({guid:guid}, function(err,obj) { 
       obj.escaped_text = notetext;
       obj.save(function(err) {
         if (err) { 
           console.log(err);
         }
       }); 
console.log(notetext);

var options = {
  mode: 'text',
  args: [notetext, 'computers,programming']
};

PythonShell.run('../python/main.py', options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  result = results[0];
  result = result.split(','); 
  // var result =   ('%s', results);
 res.render('flashcard', {


     title: obj.name,
     notetext: notetext,
     question: result[0],
     answer: result[1],
   });
})
 });
});
};

