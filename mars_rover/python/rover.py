class Rover(object):

    DIRECTIONS = {'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
    ORIENTATIONS = {'N': ('E','W'),
                    'E': ('S','N'),
                    'S': ('W','E'),
                    'W': ('N','S')}
    MAP_X = 3
    MAP_Y = 3
    x = 0
    y = 0
    orientation = 'N'
    obstacles = []
    

    def __init__(self, start_x, start_y, orientation, obstacles=[]):
        self.x = start_x
        self.y = start_y
        self.orientation = orientation
        self.obstacles = obstacles

    def move(self, movs):
        for m in movs:
            try:
                if m == 'f':
                    self.move_forward()
                elif m == 'b':
                    self.move_backwards()
                elif m == 'r':
                    self.turn_right()
                else:
                    self.turn_left()
            except Exception as e:
                print(e)
                break        

    
    def move_forward(self):
        expected_x = (self.x + self.DIRECTIONS[self.orientation][0]) % self.MAP_X
        expected_y = (self.y + self.DIRECTIONS[self.orientation][1]) % self.MAP_Y

        if self.isObstacle(expected_x,expected_y):
            raise Exception("There's an obstacle in your way")
        else:
            self.x = expected_x
            self.y = expected_y

    def move_backwards(self):
        expected_x = (self.x - self.DIRECTIONS[self.orientation][0]) % self.MAP_X
        expected_y = (self.y - self.DIRECTIONS[self.orientation][1]) % self.MAP_Y

        if self.isObstacle(expected_x,expected_y):
            raise Exception("There's an obstacle in your way")
        else:
            self.x = expected_x
            self.y = expected_y

    def turn_right(self):
        self.orientation = self.ORIENTATIONS[self.orientation][0]

    def turn_left(self):
        self.orientation = self.ORIENTATIONS[self.orientation][1]

    def isObstacle(self, x_rover, y_rover):
        return (x_rover,y_rover) in self.obstacles
