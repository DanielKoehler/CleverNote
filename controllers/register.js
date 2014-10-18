var User = require('../models/User');

exports.index = function(req, res) {
  var token =req.param('token');
  res.render('register', {
    title: 'Register',
    oauth_token: token,
  });
};

exports.register = function(req, res, next) {
  req.assert('email', 'Email is not valid').isEmail();
  req.assert('password', 'Password must be at least 4 characters long').len(4);
  req.assert('confirmPassword', 'Passwords do not match').equals(req.body.password);

  var errors = req.validationErrors();

  if (errors) {
    req.flash('errors', errors);
    return res.redirect('/evernote/signup');
  }

  var user = new User({
    email: req.body.email,
    password: req.body.password,
    oauth_token: req.body.oauth_token
  });

  User.findOne({ email: req.body.email }, function(err, existingUser) {
    if (existingUser) {
      req.flash('errors', { msg: 'Account with that email address already exists.' });
      return res.redirect('/evernote/signup');
    }
    user.save(function(err) {
      if (err) return next(err);
      req.logIn(user, function(err) {
        if (err) return next(err);
        res.redirect('/');
      });
    });
  });
};
