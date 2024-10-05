fun main() {
  val results = mutableListOf<Int>()
  while (true) {
    val n = readln().toInt()
    if (n == 0) break

    val map = mutableListOf<List<Int>>()
    repeat(n) {
      val row = readln().split(" ").map { it.toInt() }
      map.add(row)
    }

    val result = solution(n, map)
    results.add(result)
  }

  results.forEachIndexed { index, result ->
    println("Problem ${index + 1}: ${result}")
  }
}

fun solution(n: Int, map: List<List<Int>>): Int {
  val moves = listOf(-1 to 0, 1 to 0, 0 to -1, 0 to 1)

  val lostRupee = mutableMapOf<Pair<Int/*row*/, Int/*column*/>, Int/*value*/>()
  lostRupee[0 to 0] = map[0][0]

  val queue = ArrayDeque<Pair<Int/*row*/, Int/*column*/>>()
  queue.add(0 to 0)
  while (queue.isNotEmpty()) {
    val (row, col) = queue.removeFirst()
    repeat(4) { i ->
      val (dr, dc) = moves[i]
      val nr = row + dr
      val nc = col + dc

      if (nr < 0 || nc < 0 || nr >= n || nc >= n) {
        return@repeat
      }

      if (lostRupee[row to col]!! + map[nr][nc] < lostRupee.getOrDefault(nr to nc, Int.MAX_VALUE)) {
        lostRupee[nr to nc] = lostRupee[row to col]!! + map[nr][nc]
        queue.add(nr to nc)
      }
    }
  }

  return lostRupee[n-1 to n-1]!!
}