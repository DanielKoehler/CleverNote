var Evernote = require('evernote').Evernote;
var User = require('../models/User');
var Notebook = require('../models/Notebook');
exports.index = function(req, res) {
  console.log(req.user.email);
  console.log(req.user.oauth_token);
  var client = new Evernote.Client({token: req.user.oauth_token});
  var noteStore = client.getNoteStore();
  notebooks = noteStore.listNotebooks(function(err, notebooks) {
  for ( var i in notebooks) {
        Notebook.find({guid:notebooks[i].guid},function(err,res){
           if (!res.length) {
             console.log(1);
               var notebook = new Notebook({
              name: notebooks[i].name,
              user_email: req.user.email,
              guid: notebooks[i].guid

              });
              notebook.save(function(err){
                 console.log(2);
               });

           }
          
        });

   } 
  res.render('notebooks', { 
     title: 'Notebooks',
     notebooks: notebooks
   });
 });


};

