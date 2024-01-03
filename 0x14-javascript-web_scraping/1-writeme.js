#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];
const fileContent = process.argv[3];
fs.writeFile(fileName, fileContent, error => {
  if (error) {
    console.log(error);
  }
});
