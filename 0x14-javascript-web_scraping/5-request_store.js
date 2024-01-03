#!/usr/bin/node
const url = process.argv[2];
const fileName = process.argv[3];
const fs = require('fs');
const request = require('request');
request(url).pipe(fs.createWriteStream(fileName));
