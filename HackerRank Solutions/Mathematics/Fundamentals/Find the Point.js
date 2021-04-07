'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(str => str.trim());

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the findPoint function below.
 */
function findPoint(px, py, qx, qy) {
    return [2 * qx - px, 2 * qy - py];
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    for (let nItr = 0; nItr < n; nItr++) {
        const pxPyQxQy = readLine().split(' ');

        const px = parseInt(pxPyQxQy[0], 10);

        const py = parseInt(pxPyQxQy[1], 10);

        const qx = parseInt(pxPyQxQy[2], 10);

        const qy = parseInt(pxPyQxQy[3], 10);

        let result = findPoint(px, py, qx, qy);

        ws.write(result.join(" ") + "\n");
    }

    ws.end();
}
