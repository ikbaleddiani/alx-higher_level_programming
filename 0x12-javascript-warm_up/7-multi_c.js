#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < parseInt(process.argv[2])) {
    console.log('C is fun');
    i++;
  }
}
