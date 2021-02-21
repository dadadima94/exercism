object MatchingBrackets {

  val brackets: Seq[Char] = Seq('(', ')', '[', ']', '{', '}')
  val mapping: Map[Char, Int] = Map('(' -> 1, ')' -> -1, '[' -> 1, ']' -> -1, '{' -> 1, '}' -> -1)

  def isPaired(string: String): Boolean = {
    var sum = 0
    string.toList
      .map(elem => mapping.getOrElse(elem, None))
      .filter(_.isInstanceOf[Int]).map(_.toString.toInt)
      .foreach(x => if (sum >= 0) sum += x)
    if (sum == 0) true else false
  }

}