fun main() {
  val (키워드_개수, 글_개수) = readln().split(" ").map { it.toInt() }

  val 키워드들 = mutableMapOf<String, Boolean>()
  repeat(키워드_개수) {
    val 키워드 = readln()
    키워드들[키워드] = true
  }

  val 글에_사용된_키워드들 = mutableListOf<List<String>>()
  repeat(글_개수) {
    val 키워드들 = readln().split(",")
    글에_사용된_키워드들.add(키워드들)
  }

  val 결과들 = solution(키워드_개수, 키워드들, 글에_사용된_키워드들)
  결과들.forEach { 결과 ->
    println(결과)
  }
}

fun solution(키워드_개수: Int, 키워드들: Map<String, Boolean>, 글에_사용된_키워드들: List<List<String>>): List<Int> {
  var 남은_키워드_개수 = 키워드_개수
  val 남은_키워드들 = 키워드들.toMutableMap()

  val 결과 = mutableListOf<Int>()
  글에_사용된_키워드들.forEach { 사용된_키워드들 ->
    사용된_키워드들.forEach { 키워드 ->
      if (남은_키워드들.getOrDefault(키워드, false)) {
        남은_키워드들[키워드] = false
        남은_키워드_개수 -= 1
      }
    }
    결과.add(남은_키워드_개수)
  }
  
  return 결과
}