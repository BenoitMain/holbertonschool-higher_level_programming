#!/usr/bin/node
// Get command line arguments, excluding 'node' and script name
const args = process.argv.slice(2);
// Check the number of arguments and display appropriate message
if (args.length === 0) {
    console.log('No argument');
} else if (args.length === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
