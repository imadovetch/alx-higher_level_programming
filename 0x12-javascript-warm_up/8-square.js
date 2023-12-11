#!/usr/bin/node
const size = parseInt(process.argv[2]);
let square;
if ((size)) {
  for (let i = 0; i < size; i++) {
    square = '';
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
