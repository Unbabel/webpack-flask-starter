function stringReverse(text) {
  let splitText = text.split('');
  splitText = splitText.reverse();
  return splitText.join('');
}

export default stringReverse;
