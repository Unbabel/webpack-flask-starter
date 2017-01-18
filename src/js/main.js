/* global document */
import $ from 'jquery';

const reversibleMessage = $('.js-reversible-message');

$(document).on('click', '.js-reverse-message', (e) => {
  e.preventDefault();
  let text = reversibleMessage.text();
  let splitText = text.split('');
  splitText = splitText.reverse();
  text = splitText.join('');
  reversibleMessage.text(text);
});
