var Evernote = require('evernote').Evernote;
var User = require('../models/User');
var Notebook = require('../models/Notebook');
exports.index = function(req, res) {
  var client = new Evernote.Client({token: req.user.oauth_token});
  var noteStore = client.getNoteStore();
  notebooks = noteStore.listNotebooks(function(err, notebooks) {
for (var i in notebooks) {
           
               console.log(notebooks[i]);
              var notebook = new Notebook({
              name: notebooks[i].name,
              user_email: req.user.email,
              guid: notebooks[i].guid
            
              });
             notebook.save(function(err){
            if (err) {
                 console.log(err);
                }
            });
           }
  res.render('notebooks', { 
     title: 'Notebooks',
     notebooks: notebooks
   });
});
 };



	



