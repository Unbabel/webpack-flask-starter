/* global document */
/*
 * Sample string reverse function
 */
import $ from 'jquery';
import stringReverse from './string-reverse';

const reversibleMessage = $('.js-reversible-message');

$(document).on('click', '.js-reverse-message', (e) => {
  e.preventDefault();
  const text = reversibleMessage.text();
  const reversedString = stringReverse(text);
  reversibleMessage.text(reversedString);
});
