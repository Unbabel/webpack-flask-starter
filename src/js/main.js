/* global document */
/*
 * Sample string reverse function
 */
import jQuery from 'jquery';
import stringReverse from './string-reverse';

// Make jQuery available for bootstrap
window.jQuery = jQuery;

const reversibleMessage = jQuery('.js-reversible-message');

jQuery(document).on('click', '.js-reverse-message', (e) => {
  e.preventDefault();
  const text = reversibleMessage.text();
  const reversedString = stringReverse(text);
  reversibleMessage.text(reversedString);
});
