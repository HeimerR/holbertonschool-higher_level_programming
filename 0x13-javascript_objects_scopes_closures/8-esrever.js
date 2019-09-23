#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 0; i < list.length; i++) {
    const tmp = list.pop();
    list.splice(i, 0, tmp);
  }
  return list;
};
