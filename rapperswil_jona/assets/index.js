// vendor components
require('styr.css');

// application styles
require('./css/style.styl');
require('./css/layout.styl');
require('./css/typography.styl');


var FontFaceObserver = require('fontfaceobserver.js');
var font;

font = new FontFaceObserver('Roboto Slab');
font.load().then(function() {
  document.body.classList.add('slab-loaded');
});

font = new FontFaceObserver('Open Sans');
font.load().then(function() {
  document.body.classList.add('sans-loaded');
});
