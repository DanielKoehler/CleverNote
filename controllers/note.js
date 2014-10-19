var Evernote = require('evernote').Evernote;
var User = require('../models/User');
var Note = require('../models/Note');
var PythonShell = require('python-shell');

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
var options = {
  mode: 'text',
  args: ['5', obj.name, 'computer science programming']
};

PythonShell.run('../python/content_finder.py', options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
  obj.wiki_array = results;
         obj.save(function(err) {
         if (err) {
           console.log(err);
         }
       });

});
var wiki_array = "";
if (obj.wiki_array){
wiki_array = obj.wiki_array.split(',');
}

console.log(wiki_array); 
 res.render('note', { 


     title: obj.name,
     notetext: notetext,
     wiki: wiki_array,
   });
 });
});
};

