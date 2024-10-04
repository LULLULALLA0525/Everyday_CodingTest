fun main() {
  val (n, m) = readln().split(" ").map { it.toInt() }

  val costs = mutableListOf<List<Int>>()
  repeat(n) {
    val row = readln().split(" ").map { it.toInt() }
    costs.add(row)
  }

  val result = solution(n, m, costs)
  println(result)
}

data class DP(
  val fromLeft: Int = Int.MAX_VALUE,
  val fromMiddle: Int = Int.MAX_VALUE,
  val fromRight: Int = Int.MAX_VALUE
) {
  fun minValue(): Int = minOf(fromLeft, fromMiddle, fromRight)
}

fun solution(n: Int, m: Int, costs: List<List<Int>>): Int {
  val dp = mutableListOf<List<DP>>()

  costs.forEachIndexed { row, cols ->
    val rowDp = mutableListOf<DP>()
    cols.forEachIndexed { col, cost ->
      if (row == 0) {
        rowDp.add(
          DP(cost, cost, cost)
        )
      } else {
        if (col == 0) {
          val middle = dp[row - 1][col]
          val right = dp[row - 1][col + 1] 
          rowDp.add(
            DP(
              fromMiddle = middle.fromRight + cost, 
              fromRight = minOf(right.fromLeft, right.fromMiddle) + cost
            )
          )
        } else if (col == m - 1) {
          val left = dp[row - 1][col - 1]
          val middle = dp[row - 1][col]
          rowDp.add(
            DP(
              fromLeft = minOf(left.fromMiddle, left.fromRight) + cost, 
              fromMiddle = middle.fromLeft + cost
            )
          )
        } else {
          val left = dp[row - 1][col - 1]
          val middle = dp[row - 1][col]
          val right = dp[row - 1][col + 1]
          rowDp.add(
            DP(
              fromLeft = minOf(left.fromMiddle, left.fromRight) + cost,
              fromMiddle = minOf(middle.fromLeft, middle.fromRight) + cost,
              fromRight = minOf(right.fromLeft, right.fromMiddle) + cost
            )
          )
        }
      }
    }
    dp.add(rowDp)
  }

  val answer = dp[n - 1].map { it.minValue() }.min()

  return answer
}