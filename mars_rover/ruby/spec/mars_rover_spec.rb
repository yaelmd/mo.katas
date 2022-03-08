require 'rover'

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

describe 'Mars rover' do
  context 'facing north' do
    it 'moves forwards' do
      rover = Rover.new(1, 1, :north)
      movements = ['f']

      rover.move(movements)

      expect(rover.x).to eq(1)
      expect(rover.y).to eq(2)
      expect(rover.orientation).to eq(:north)
    end

    it 'moves backwards' do
      rover = Rover.new(1, 1, :north)
      movements = ['b']

      rover.move(movements)

      expect(rover.x).to eq(1)
      expect(rover.y).to eq(0)
      expect(rover.orientation).to eq(:north)
    end
  end
end