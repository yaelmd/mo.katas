import unittest

from rover import Rover

"""
Mars rover moves through


                       N
        --------------------------------
        |   0,2   |   1,2   |   2,2    |
        -------------------------------- 
    W   |   0,1   |   1,1   |   2,1    |    E
        -------------------------------- 
        |   0,0   |   1,0   |   2,0    |
        --------------------------------
                       S
                   
"""


class MarsRoverTestCase(unittest.TestCase):


    def test_multiple_movements(self):
        rover = Rover(
            start_x = 1,
            start_y = 1,
            orientation = 'N',
            obstacles = [(0,1),(1,2),(0,0)]
        )
        movements = ['r','f','l','b','b','r','f','r','f','l','f','f','f']
        expected_position = (0,2)
        rover.move(movements)
        self.assert_rover_position(expected_position,rover)

    #Movements with obstacles

    def test_rover_move_backwards_obstacle(self):
        rover = Rover(
            start_x = 2,
            start_y = 2,
            orientation = 'W',
            obstacles = [(0,1),(0,2)]
        )
        movements = ['b']
        expected_position = (2,2)
        rover.move(movements)
        self.assert_rover_position(expected_position,rover)

    def test_rover_move_forward_obstacle(self):
        rover = Rover(
            start_x = 0,
            start_y = 0,
            orientation = 'N',
            obstacles = [(0,1),(1,2)]
        )
        movements = ['f']
        expected_position = (0,0)
        rover.move(movements)
        self.assert_rover_position(expected_position,rover)


    #Move backwards outside the borders

    def test_rover_move_backwards_north_border(self):
        rover = Rover(
            start_x=0,
            start_y=0,
            orientation = 'N'
        )
        movements = ['b']
        expected_position = (0,2)
        rover.move(movements)

        self.assert_rover_position(expected_position, rover)

    def test_rover_move_backwards_east_border(self):
        rover = Rover(
            start_x=0,
            start_y=2,
            orientation = 'E'
        )
        movements = ['b']
        expected_position = (2,2)
        rover.move(movements)

        self.assert_rover_position(expected_position, rover)


    #Move forward outside the borders

    def test_rover_move_forward_south_border(self):
        rover = Rover(
            start_x=2,
            start_y=0,
            orientation='S'
        )

        movements = ['f']
        expected_position = (2,2)
        rover.move(movements)

        self.assert_rover_position(expected_position, rover)
    

    def test_rover_move_forward_west_border(self):
        rover = Rover(
            start_x=0,
            start_y=0,
            orientation='W'
        )

        movements = ['f']
        expected_position = (2,0)
        rover.move(movements)

        self.assert_rover_position(expected_position, rover)

    #Move forward inside the borders

    def test_rover_move_forward_east(self):

        rover = Rover(
            start_x=1,
            start_y=1,
            orientation='E'
        )

        movements = ['f']
        expected_position = (2, 1)
        rover.move(movements)

        self.assert_rover_position(expected_position, rover)

    def test_rover_move_forward_south(self):
        rover = Rover(
            start_x=1,
            start_y=1,
            orientation='S'
        )

        movements = ['f']
        expected_position = (1, 0)
        rover.move(movements)

        self.assert_rover_position(expected_position, rover)

    
    #Move backwards inside the borders

    def test_rover_move_backwards_north(self):
        rover = Rover(
            start_x=1,
            start_y=1,
            orientation='N'
        )

        movements = ['b']
        expected_position = (1, 0)
        rover.move(movements)

        self.assert_rover_position(expected_position, rover)

    def test_rover_move_backwards_east(self):
        rover = Rover(
            start_x=1,
            start_y=1,
            orientation='E'
        )

        movements = ['b']
        expected_position = (0, 1)
        rover.move(movements)

        self.assert_rover_position(expected_position, rover)


    #Turn right

    def test_rover_turn_right(self):
        rover = Rover(
            start_x=1,
            start_y=1,
            orientation='N'
        )

        movements = ['r','r','r']
        expected_orientation = 'W'
        rover.move(movements)
        self.assert_rover_orientation(expected_orientation, rover)
        movements = ['r']
        expected_orientation = 'N'
        rover.move(movements)
        self.assert_rover_orientation(expected_orientation, rover)


    #Turn left

    def test_rover_turn_left(self):
        rover = Rover(
            start_x=1,
            start_y=1,
            orientation='N'
        )

        movements = ['l','l','l']
        expected_orientation = 'E'
        rover.move(movements)
        self.assert_rover_orientation(expected_orientation, rover)
        movements = ['l']
        expected_orientation = 'N'
        rover.move(movements)
        self.assert_rover_orientation(expected_orientation, rover)

        
    def assert_rover_position(self, expected_position, rover):
        self.assertEqual(expected_position[0], rover.x)
        self.assertEqual(expected_position[1], rover.y)
    
    def assert_rover_orientation(self, expected_orientation, rover):
        self.assertEqual(expected_orientation, rover.orientation)


if __name__ == '__main__':
    unittest.main()