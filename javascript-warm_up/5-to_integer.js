#!/usr/bin/node

// Convert the first command line argument to an integer
const num = parseInt(process.argv[2]);
// Check if the conversion resulted in a valid number
if (isNaN(num)) {
  // If not a number, display error message
  console.log('Not a number');
} else {
  // If valid number, display the integer value
  console.log('My number: ' + num);
}
