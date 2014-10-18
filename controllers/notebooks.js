var Evernote = require('evernote').Evernote;
var User = require('../models/User');

exports.index = function(req, res) {
  console.log(req.user.email);
  console.log(req.user.oauth_token);
  var client = new Evernote.Client({token: req.user.oauth_token});
  var noteStore = client.getNoteStore();
  notebooks = noteStore.listNotebooks(function(err, notebooks) {
   res.render('notebooks', { 
     title: 'Notebooks',
     notebooks: notebooks,

   });
 });


};

