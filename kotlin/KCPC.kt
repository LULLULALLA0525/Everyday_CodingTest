fun main() {
  val 테스트케이스_개수 = readln().toInt()
  val 결과들 = mutableListOf<Int>()
  repeat(테스트케이스_개수) {
    val (팀_개수, 문제_개수, 내_팀_ID, 제출_개수) = readln().split(" ").map{ it.toInt() }

    val 제출들 = mutableListOf<제출_로그>()
    repeat(제출_개수) {
      val (팀_ID, 문제_번호, 점수) = readln().split(" ").map{ it.toInt() }
      제출들.add(
        제출_로그(팀_ID, 문제_번호, 점수)
      )
    }

    val 결과 = solution(팀_개수, 문제_개수, 내_팀_ID, 제출_개수, 제출들)
    결과들.add(결과)
  }

  결과들.forEach { 결과 ->
    println(결과)
  }
}

data class 제출_로그(
  val 팀_ID: Int,
  val 문제_번호: Int,
  val 점수: Int
)

data class 팀_정보(
  val 문제별_점수: Map<Int/*문제_번호*/, Int/*점수*/> = mapOf(),
  val 제출_개수: Int = 0,
  val 마지막_제출_시간: Int = Int.MAX_VALUE
)

fun solution(팀_개수: Int, 문제_개수: Int, 내_팀_ID: Int, 제출_개수: Int, 제출들: List<제출_로그>): Int {
  val 팀들 = mutableMapOf<Int/*팀_ID*/, 팀_정보>()

  제출들.forEachIndexed { 시간, 제출 ->
    val 기존_팀_정보 = 팀들.getOrDefault(제출.팀_ID, 팀_정보())
    
    val 문제별_점수 = 기존_팀_정보.문제별_점수.toMutableMap()
    문제별_점수[제출.문제_번호] = maxOf(문제별_점수.getOrDefault(제출.문제_번호, 0), 제출.점수)

    팀들[제출.팀_ID] = 팀_정보(
      문제별_점수 = 문제별_점수,
      제출_개수 = 기존_팀_정보.제출_개수 + 1,
      마지막_제출_시간 = 시간
    )
  }

  val 팀_순위 = 팀들.toList().sortedWith(
    compareBy(
      { -it.second.문제별_점수.values.sum() },
      { it.second.제출_개수 },
      { it.second.마지막_제출_시간 }
    )
  ).map { it.first }

  return 팀_순위.indexOf(내_팀_ID) + 1
}