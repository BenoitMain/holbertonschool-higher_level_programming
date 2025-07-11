#!/usr/bin/node

// Convert the first command line argument to an integer
const X = parseInt(process.argv[2]);
// Check if the conversion resulted in a valid number
if (isNaN(X)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < X; i++) {
    console.log('C is fun');
  }
}
