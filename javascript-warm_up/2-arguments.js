#!/usr/bin/node
const args = process.argv.length - 2;

if (args.length === 0) {
    console.log('No argument');
} else if (args.length === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
