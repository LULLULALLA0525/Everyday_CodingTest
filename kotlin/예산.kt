fun main() {
  val n = readln().toInt()
  val 요청들 = readln().split(" ").map { it.toInt() }
  val 예산 = readln().toInt()
  
  val 결과 = solution(요청들, 예산)
  println(결과)
}

fun solution(요청들: List<Int>, 예산: Int): Int {
  var 남은_예산 = 예산
  var 남은_요청들 = 요청들

  var 지급함 = true
  val 지급한_요청들 = mutableListOf<Int>()
  while (남은_요청들.isNotEmpty()) {
    지급함 = false

    var 지급되는_예산 = 남은_예산 / 남은_요청들.size
    val 부족한_요청들 = mutableListOf<Int>()

    남은_요청들.forEach { 요청 ->
      if (요청 < 지급되는_예산) {
        남은_예산 -= 요청
        지급한_요청들.add(요청)
        지급함 = true
      } else {
        부족한_요청들.add(요청)
      }
    }

    남은_요청들 = 부족한_요청들

    if (!지급함) {
      return 지급되는_예산
    }
  }

  return 지급한_요청들.max()
}