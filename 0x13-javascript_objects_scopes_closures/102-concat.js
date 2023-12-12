#!/usr/bin/node
const fs = require('fs').promises;
const { argv } = require('process');
const fOne = argv[2];
const fTwo = argv[3];
const fThree = argv[4];
async function concatTwoFiles () {
  try {
    const data1 = await fs.readFile(fOne);
    const data2 = await fs.readFile(fTwo);
    fs.writeFile(fThree, data1 + data2);
  } catch (err) {
    console.log(err);
  }
}
concatTwoFiles();
