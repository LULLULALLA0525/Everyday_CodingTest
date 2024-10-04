fun main() {
  val 테스트케이스_개수 = readln().toInt()

  val 결과들 = mutableListOf<Long>()
  repeat(테스트케이스_개수) {
    val 주가_개수 = readln().toInt()
    val 주가들 = readln().split(" ").map { it.toLong() }
    
    val 결과 = solution(주가_개수, 주가들)
    결과들.add(결과)
  }

  결과들.forEach { 결과 ->
    println(결과)
  }
}

fun solution(주가_개수: Int, 주가들: List<Long>): Long {
  var 피크들 = mutableListOf<Pair<Int/*인덱스*/, Long/*주가*/>>()
  주가들.forEachIndexed { 인덱스, 주가 ->
    피크들 = 피크들.filter { it.second > 주가 }.toMutableList()
    피크들.add(인덱스 to 주가)
  }

  var 결과 = 0L
  주가들.forEachIndexed { 인덱스, 주가 ->
    val 피크 = 피크들.find { it.first >= 인덱스 }
    if (피크 != null) {
      val 차이 = 피크.second - 주가
      if (차이 > 0) {
        결과 += 차이
      }
    }
  }

  return 결과
}