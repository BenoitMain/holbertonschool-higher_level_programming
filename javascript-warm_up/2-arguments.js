#!/usr/bin/node

// Get command line arguments, excluding 'node' and script name
const args = process.argv.slice(2);

// Check the number of arguments and display appropriate message
if (args.length === 0) {
    // No arguments provided
    console.log('No argument');
} else if (args.length === 1) {
    // Exactly one argument provided
    console.log('Argument found');
} else {
    // Multiple arguments provided
    console.log('Arguments found');
}
