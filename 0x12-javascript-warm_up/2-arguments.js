#!/usr/bin/node
const myVar = process.argv;
if (myVar.length === 1) {
  console.log('No argument');
} else if (myVar.length === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
