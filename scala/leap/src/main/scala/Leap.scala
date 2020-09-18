object Leap {
  def leapYear(year: Int): Boolean = {

    val isDivisibleBy: (Int) => Boolean = year % _ == 0

    isDivisibleBy(4) && (!isDivisibleBy(100) || isDivisibleBy(400))
    }
  }
