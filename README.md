# Conway-s-Game-of-Live
Game of Life is a cell-based automaton game devised by John Horton Conway. 
[Check the wiki for more details.](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

This version was made in Python using pygame library.

### Rules
- Any live cell with two or three live neighbours survives.
- Any dead cell with three live neighbours becomes a live cell.
- All other live cells die in the next generation. Similarly, all other dead cells stay dead.


### How to Play
To play, first install dependencies however you like. Then simply run game.py via terminal:
```
python game.py
```

Initially, you'll get a canvas of all dead cells. You can "paint" live cells to the canvas.
You have four buttons at your disposal.
- Green button will play the simulation.
- Orange button will pause the simulation.
- Red button will stop the simulation and clear the board.
- Blue button will increment the simulation by a single step.

There is a slider on the bottom right for fps adjustment. You can click on any place in it to change the speed of the game accordingly.
