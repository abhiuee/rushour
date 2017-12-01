# rushour
Python Game using pygame. Based on the boardgame http://www.thinkfun.com/products/rush-hour/
Goal of the game is to slide the red car to the exit (white block). Vehicles can move up and down or right and left in their lanes. Click on the vehicle and point to the position of the top left corner of the car. The game can also be played with a text verion in which the grid is represented by a 6x6 matrix. The console tells you whether the move that you made is successful or not. 

## How to load the game
>python3 rushour.py game0.txt

## Game files
The game is loaded using a text file. Sample file

h, 2, 2, 0 <br>
v, 2, 0, 0 <br>
h, 3, 0, 1 <br>
v, 3, 0, 5

Here column 1, means the orientation of car, if 'h' then car can only move right and left, if 'v' car can only move up and down. Second column is the width of the car. Column 3 and Column 4, mark the top-left corner of the car in the grid.

## Game Requirements
* [pygame](https://www.pygame.org/)
* python3

## Sample Game Images

### Initial Game
![Initial Game Image](/images/initial.png)

