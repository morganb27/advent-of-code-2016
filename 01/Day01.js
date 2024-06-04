const fs = require('fs');

function readFile(file_path) {
    const content = fs.readFileSync(file_path, 'utf-8');
    const directions = content.split(', ');
    return directions;
}

const data = readFile("input.txt");

function findEasterBunnyHQPosition() {
    let mySet = new Set();
    const position = {
        x: 0,
        y: 0,
        facing: 'N'
    }
    mySet.add(`${position.x},${position.y}`);
    for (let i = 0; i < data.length; i++) {
        let turn = data[i].charAt(0);
        let steps = parseInt(data[i].substring(1));

        if (position.facing == 'N') {
            position.facing = turn == 'R' ? 'E' : 'W'
        } else if (position.facing == 'E') {
            position.facing = turn == 'R' ? 'S' : 'N';
        } else if (position.facing == 'S') {
            position.facing = turn == 'R' ? 'W' : 'E';
        } else if (position.facing == 'W') {
            position.facing = turn == 'R' ? 'N' : 'S';
        }

        for (let i = 0; i < steps; i++) {
            console.log(mySet);
            if (position.facing == 'N') {
                position.y++;
                const locationVisited = keepTrackOfAlllocations(position.x, position.y, mySet);
                if (locationVisited) {
                    return locationVisited;
                }
            } else if (position.facing == 'E') {
                position.x++;
                const locationVisited = keepTrackOfAlllocations(position.x, position.y, mySet);
                if (locationVisited) {
                    return locationVisited;
                }
            } else if (position.facing == 'S') {
                position.y--;
                const locationVisited = keepTrackOfAlllocations(position.x, position.y, mySet);
                if (locationVisited) {
                    return locationVisited;
                }
            } else if (position.facing == 'W') {
                position.x--;
                const locationVisited = keepTrackOfAlllocations(position.x, position.y, mySet);
                if (locationVisited) {
                    return locationVisited;
                }
            }
        }
        
    }
    console.log("position", position)
    return position;
}


function keepTrackOfAlllocations(x, y, set) {
    let currentPosition = `${x},${y}`
    if (!set.has(currentPosition)) {
        set.add(currentPosition);
    } else {
        return currentPosition;
    }
}


console.log(findEasterBunnyHQPosition());

