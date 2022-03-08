class Rover
  attr_reader :x, :y, :orientation

  def initialize(start_x, start_y, orientation)
      @x = start_x
      @y = start_y
      @orientation = orientation
  end

  def move(movs)
    movs.each do |m|
        if @orientation == :north
          if m == 'f'
              @y = @y + 1
          elsif m == 'b'
              @y = @y - 1
          end
        end
      end
    end
  end