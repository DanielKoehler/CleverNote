var Evernote = require('evernote').Evernote;
var User = require('../models/User');
var Notebook = require('../models/Notebook');

exports.notebooks = function(req, res) {
  Notebook.find({user_email: req.user.email}, function(err,notebook) {
     
  if (err) return console.error(err);
    console.log(notebook);
    res.json(notebook);
  });   
};


exports.note = function(req, res) {
  res.render('home', {
    title: 'Home'
  });
};

exports.notes = function(req, res) {
  res.render('home', {
    title: 'Home'
  });
};

