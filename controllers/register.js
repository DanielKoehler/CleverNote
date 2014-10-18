/**
 * GET /
 * Home page.
 */

exports.index = function(req, res) {
  console.log(req.param('token'))
  res.render('register', {
    title: 'Register'
  });
};

