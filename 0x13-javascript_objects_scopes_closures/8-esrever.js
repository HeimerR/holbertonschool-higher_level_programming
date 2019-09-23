#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 0; i < list.length / 2 + 1; i++) {
    const tmp = list.pop();
    list.splice(i, 0, tmp);
  }
  return list;
};
