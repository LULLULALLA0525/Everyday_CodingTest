fun main() {
  val numbers = readln().map { it.toString().toInt() }

  val result = solution(numbers)
  println(result)
}

data class DP(val max: Int, val available: List<Pair<Int, Boolean>>)

fun solution(numbers: List<Int>): Int {
  val dp = mutableListOf<DP>()

  numbers.forEachIndexed { i, number ->
    val prev = if (i == 0) DP(max = 0, available = listOf(0 to false)) else dp[i - 1]

    val digit = prev.available.indexOf(number to true)
    if (digit == -1) {
      var current = prev.max + 1
      var new_digit = -1
      while (true) {
        new_digit = "$current".indexOf("$number")
        if (new_digit != -1) break
        current++
      }

      val available = "$current".mapIndexed { ii, value ->
        value.toString().toInt() to (ii > new_digit)
      }

      dp.add(DP(
        max = current,
        available = available
      ))
    } else {
      val available = "${prev.max}".mapIndexed { ii, value ->
        value.toString().toInt() to (ii > digit)
      }

      dp.add(DP(
        max = prev.max, 
        available = available
      ))
    }    
  }

  return dp.last().max
}