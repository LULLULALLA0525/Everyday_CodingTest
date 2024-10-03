fun main(args: Array<String>) {
  val n = readln().toInt()
  val edges = readln().split(" ").map { it.toInt() }
  val costs = readln().split(" ").map { it.toInt() }

  val result = solution(n, edges, costs)
  println(result)
}

fun solution(n: Int, edges: List<Int>, costs: List<Int>): Int {
  var answer = 0

  var minCost = Int.MAX_VALUE
  for (i in 0..(n - 2)) {
    if (costs[i] < minCost) {
      minCost = costs[i]
    }

    answer += edges[i] * minCost
  }
  
  return answer
}