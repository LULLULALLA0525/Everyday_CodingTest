fun main(args: Array<String>) {
  val n = readln().toInt()

  val result = solution(n)
  println(result)
}

fun solution(n: Int): Int {
  var list = (1..n).toList()

  var removeOdd = true
  while (list.size > 1) {
    val filteredList = list.filterIndexed { index, _ -> index % 2 == if (removeOdd) 1 else 0 }
    removeOdd = if (list.size % 2 == 0) removeOdd else !removeOdd
    list = filteredList
  }

  return list[0]
}