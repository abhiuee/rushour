"""

Notes:
- Game is modelled based on demonstration of the game uploaded on Piazza
- Empty points on the grid are marked with "."
- The car the user is in control of is #0
- The win condition is when the right most value of car 0 is in position row 2, column 5 on the grid
- Please use the left (for horizontal cars) and top (vertical cars) most value as the point of reference when moving car to the new point. 

A sample of what the game looks like for game0.txt :

Col:    0 1 2 3 4 5
Row:  -------------
 0   |  1 2 2 2 . 3
 1   |  1 . 4 5 . 3
 2   |  0 0 4 5 . 3
 3   |  . . 4 6 7 7
 4   |  . 8 8 6 9 .
 5   |  . 10 10 10 9 . 

"""
import sys
#needed for sys.argv 
import pygame
#needed for graphics

class rusHour():
    #mainclass rusHour where the text-game will be ran 
    grid = []
    carlist = []
    #creates two new lists (class variables), grid keeps track of the grid the user sees, while carlist contains the car paramters for the given game#.txt file

    def __init__(self):
        #class constructor - create an empty grid and parse command line options
        rusHour.grid = [['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.']]
        #set class variable grid equal to a 6x6 grid with each inital entry at "." will be updated when the game is loaded and moves are made
        #a for loop was avoided to avoid unecessary complexity 
        if len(sys.argv) < 2:
            print ("[ERROR] Please provide the game file to load the game")
            exit()
            #for invalid inputs, when user inputs "rushour.py" into the command line with no game.txt file
        else:
            self.gamefile = sys.argv[1]
            #user inputs "rushour.py game#.txt" where rushour.py is argument value [0] and game#.txt is argument value [1] 

    def loadGameState(self):
        #method to load the game state from "game.txt" file
        try:
            fileVar = open(self.gamefile, 'r')
            #set a variable called fileVar to open and read the gamefile variable above
        except IOError:
            print ("[ERROR] Game file not found")
            exit()
            #Error if the gamefile is not in the directory that rushhour.py is in 
        i = 0
        #initialize a counter, i to 0 that will be incremented with each iteration of the for loop below: 
        for line in fileVar:
            #reads each line of the gamefile
            line = line.strip('\n')
            car = line.split(', ')
            #remove ',' from the line in order to create a list or car properties

            car[1] = int(car[1])
            car[2] = int(car[2])
            car[3] = int(car[3])
            #converts the size, row, and column of the car into an integer
            #the last boolean is for active or inactive car

            rusHour.carlist.append(car)
            #appends car into the class variable carlist 

            #car[0] refers to the first parameter of the car, its orientation (horizontal or vertical)
            if car[0] == 'h':
                #if the car is horizontal
                for j in range (0, car[1]):
                    #car[1] contains the width/length of the car
                    #the range is 0 to the size of the car 
                    rusHour.grid[car[2]][car[3]+j] = i
                    #add the car to the grid
                    #for horizontally oriented car the columns change while row remains same
            if car[0] == 'v':
                #if the car is vertical
                for j in range (0, car[1]):
                    #the range is 0 to the size of the car
                    rusHour.grid[car[2]+j][car[3]] = i
                    #add the car to the grid
                    #for vertically oriented car the row changes while column remains same
            i = i+1
            #after each iteration of the for loop, increase i by 1 

    def showGridState(self):
        #create a method that will print the grid that the user sees as moves are being made
        for subgrid in rusHour.grid:
            #subgrid refers to each element within grid 
            print('\t'.join('{}'.format(str(k)) for k in subgrid))
            #print each element, k in each subgrid with horizontal spacing

    def updateCarPosition(self, newPosition):
        #creates a new function that updates car position and takes 1 parameter newPosition
        #newPosition is defined under the playGame method below. it moves a car to a new position and takes arguments by the user in the form car #, row, column 
        if int(newPosition[0]) >= len(rusHour.carlist):
            print ("[ERROR] Wrong car number")
            #newPosition[0] refers to the car # that the user wishes to move. this conditional means that the user cannot move a car that does not exist 
            return
        
        if int(newPosition[1]) >= 6 or int(newPosition[2]) >= 6:
            print ("[ERROR] Wrong new position for car")
            #can not move to a row or column position outside of the grid
            return
        
        car = rusHour.carlist[int(newPosition[0])]
        #car points to the car from the carlist pointed to by the user
        new_x = int(newPosition[1])
        new_y = int(newPosition[2])
        #cache the new x, y coordinate (row, column respectively) 
        
        if car[0] == 'h':
            #if the car is horizontal 
            if new_x != car[2]:
                print ("ILLEGAL MOVE!!!!")
                #a horizontal car can not change column #'s
                return
            old_x = car[2]
            #cache old_x coordinate of the car
            old_y = car[3]
            #cache old_y coordinate of the car
            illegal_move = False
            #creates a boolean illegal_move that is initially set to False
            
            for j in range(0, car[1]):
                #the range is 0 to the size of the car
                rusHour.grid[old_x][old_y+j] = '.'
                #the row "old_x" and columns "old_y" up to the size of the car are replaced with an empty space "." 
                
            for j in range(0, car[1]):
                #the range is 0 to the size of the car
                if new_y + j >= 6:
                    #new_y cannot exceed the # of columns
                    print ("ILLEGAL MOVE!!!!")
                    illegal_move = True
                    break
                if rusHour.grid[new_x][new_y + j] != '.':
                    #if the space is not empty ("."), the car cannot move into that space 
                    print ("ILLEGAL MOVE!!!!")
                    illegal_move = True
                    break
                
            if illegal_move:
                car[2] = old_x
                car[3] = old_y
                #if illegal_move is true then the x and y coordinates of vehicle 0 remain the same and will not be updated
            else:
                car[2] = new_x
                car[3] = new_y
                #else, if illegal_move is false then the x and y coordinates of vehicle 0 will be updated to the new x and y coordinate that the user inputs
            for j in range(0, car[1]):
                rusHour.grid[car[2]][car[3]+j] = int(newPosition[0])
                #update the grid with the new/old position of the car
            if illegal_move == False:
                print ("SUCCESFUL MOVE")
                self.showGridState()
                #show the grid when valid move is made 
                
        if car[0] == 'v':
            if new_y != car[3]:
                print ("ILLEGAL MOVE!!!!")
                #the new_y coordinate of the car cannot be different from the old y coordinate of the car. That is, a vertical car cannot cannot change columns (only rows) 
                return
            old_x = car[2]
            old_y = car[3]
            #old_x and old_y take on the row and column #'s respectively if new_y == car[3] 
            illegal_move = False
            #creates a boolean illegal_move that is initially False
            
            for j in range(0, car[1]):
                #range is 0 to the size of the car 
                rusHour.grid[old_x+j][old_y] = '.'
                #after the car moves the row becomes empty
            for j in range(0, car[1]):
                #range is 0 to the size of the car
                if new_x + j >= 6:
                    print ("ILLEGAL MOVE!!!!")
                    illegal_move = True
                    #car cannot move beyond the # of rows
                    break
                if rusHour.grid[new_x+j][new_y] != '.':
                    print ("ILLEGAL MOVE!!!!")
                    illegal_move = True
                    #a car cannot move to a space that is not empty 
                    break

            if illegal_move:
                car[2] = old_x
                car[3] = old_y
                #if illegal_move is true then the x, y (row,column) coordinates remain the same
            else:
                car[2] = new_x
                car[3] = new_y
                #if illegal_move is false then the x,y (row,column) coordinates are updated 

            for j in range(0, car[1]):
                #range is 0 to the size of the car
                rusHour.grid[car[2]+j][car[3]] = int(newPosition[0])
                #update the grid with the new/old position of the car

            if illegal_move == False:
                print ("SUCCESFUL MOVE")
                self.showGridState()
                #show the grid when valid move is made

    def displayGrid(self, surface, nGrid, gridSize, active):
        surface.fill((64,64,64))
        surface.fill((255, 255, 255), (5*gridSize, 2*gridSize, gridSize, gridSize))
        i = 0
        for car in rusHour.carlist:
            if i == active: 
                color = (0, 255, 0)
            else:
                if i == 0:
                    color = (255, 0 , 0)
                else:
                    color = (0, 0, 255)
            i = i + 1
            if car[0] == 'h':
                x = car[2]
                y = car[3]
                surface.fill( color,
                            ( y * gridSize, x * gridSize, car[1]*gridSize - 5, gridSize - 5) )
            if car[0] == 'v':
                x = car[2]
                y = car[3]
                surface.fill( color,
                            ( y * gridSize, x * gridSize, gridSize - 5, car[1]*gridSize - 5) )

    def startGame(self):
        pygame.init() # Prepare the PyGame module for use
        size = 720
        surface = pygame.display.set_mode( (size, size) )
        nGrid = 6
        gridSize = size / nGrid

        active = None
        while True:
            ev = pygame.event.wait()
            if ev.type == pygame.QUIT:
                break

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 :
                x,y = ev.pos
                grid_x, grid_y = x // gridSize, y // gridSize
                grid_value = rusHour.grid[int(grid_y)][int(grid_x)]
                if active == None:
                    if grid_value != '.':
                        active = grid_value
                    else:
                        active = None
                else:
                    self.updateCarPosition([active, int(grid_y), int(grid_x)])
                    active = None

            self.displayGrid(surface, nGrid, gridSize, active)
            pygame.display.flip()
            if rusHour.carlist[0][3] == 4:
                #the win condition is the right most coordinate of car 0 entering position 2,5 on the grid
                #the left most coordinate of the car will be 2,4
                print ("SUCCESS!!!!")
        pygame.quit()

    def playGame(self):
        #creates a new method within the class called playgame 
        #this method is the main interface with the user
        user_input = input("Enter car, row, column (quit to exit):")
        #variable user_input takes user input as car, row, column 
        while user_input != "quit":
            newPosition = user_input.split(',')
            #newPosition stores the user_input and split gets rid of commas inbetween user input and only evaluates the integer arguments
            if len(newPosition) != 3:
                print ("[ERROR] Try Again. Enter Valid Input")
                #if the user does not provide 3 arguments for the newPosition as car, row, column this will prompt user for a valid input
            else:
                self.updateCarPosition(newPosition)
                #update car position for valid arguments of the form car, row, column

            if rusHour.carlist[0][3] == 4:
                #the win condition is the right most coordinate of car 0 entering position 2,5 on the grid
                #the left most coordinate of the car will be 2,4
                print ("SUCCESS!!!!")
                break
            user_input = input("Enter car, row, column (quit to exit):")

if __name__ == '__main__':
    isDebug = False
    if len(sys.argv) == 3:
        if sys.argv[2] == "debug":
            isDebug = True;
    a = rusHour()
    #creates an instance of the class
    a.loadGameState()
    if isDebug:
        print ("[INFORMATION] Game successfully loaded. Grid State is:")
        a.showGridState()
        a.playGame()
    else:
        a.startGame()
