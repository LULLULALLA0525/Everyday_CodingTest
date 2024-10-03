fun solution(a: Int, b: Int): Int {
  return a + b
}

fun main(args: Array<String>) {
  val (a, b) = readln().split(" ").map { it.toInt() }

  println(solution(a, b))
}