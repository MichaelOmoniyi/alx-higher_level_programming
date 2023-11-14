#!/usr/bin/node
/* return the reversed version of a list */
exports.esrever = function (list) {
  const rev = [];
  let index = 0;
  for (let i = (list.length - 1); i >= 0; i--) {
    rev[index] = list[i];
    index += 1;
  }
  return rev;
};
