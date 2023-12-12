#!/usr/bin/node

const dict = require('./101-data').dict;
const theNew = {};
for (const key in dict) {
  if (theNew[dict[key]] === undefined) {
    theNew[dict[key]] = [];
  }
  theNew[dict[key]].push(key);
}
console.log(theNew);
