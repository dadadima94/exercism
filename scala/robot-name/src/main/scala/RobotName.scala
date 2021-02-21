import scala.util.Random

class Robot {
  var name: String = Robot.generateName()

  def reset() =
    name = Robot.generateName()
}

object Robot {
  def generateName(): String = {
    sample('A' to 'Z', 2) ++ sample('0' to '9', 3)
  } mkString


  def sample(range: Seq[Char], length: Int): Seq[Char] = {
    Seq.fill(length) {
      range(Random.nextInt(range.length))
    }
  }
}