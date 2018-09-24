// vendor components
import 'styr';

// application styles
import './css/layout.styl';
import './css/style.styl';
import './css/typography.styl';

import FontFaceObserver from 'fontfaceobserver';
let font;

font = new FontFaceObserver('Roboto Slab');
font.load().then(() => {
  document.body.classList.add('slab-loaded');
});

font = new FontFaceObserver('Open Sans');
font.load().then(() => {
  document.body.classList.add('sans-loaded');
});
