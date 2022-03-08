class Rover {
  constructor(x, y, orientation) {
    this.x = x
    this.y = y
    this.orientation = orientation
  }

  move(movs) {
    movs.forEach(m => {
      if (m === "f") {
        this.y = this.y + 1
      } else if (m === "b") {
        this.y = this.y - 1
      }
    })
  }
}

module.exports = Rover
