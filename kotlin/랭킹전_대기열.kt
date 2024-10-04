fun main() {
  val (플레이어_수, 정원) = readln().split(" ").map { it.toInt() }
  
  val 플레이어들 = mutableListOf<Player>()
  repeat(플레이어_수) {
    val (레벨, 닉네임) = readln().split(" ")
    플레이어들.add(
      Player(
        레벨 = 레벨.toInt(),
        닉네임 = 닉네임
      )
    )
  }

  solution(플레이어들, 정원)
}

data class Player(
  val 레벨: Int,
  val 닉네임: String
)

data class Lounge(
  val 최소_레벨: Int,
  val 최대_레벨: Int,
  val 플레이어들: MutableList<Player>,
  var 상태: String
)

fun solution(플레이어들: List<Player>, 정원: Int) {
  val 게임방들 = mutableListOf<Lounge>()

  플레이어들.forEach { 플레이어 ->
    val 게임방 = 게임방들.find { it.상태 == "Waiting!" && it.최소_레벨 <= 플레이어.레벨 && 플레이어.레벨 <= it.최대_레벨 }
    
    if (게임방 != null) {
      게임방.플레이어들.add(플레이어)
      if (게임방.플레이어들.size == 정원) {
        게임방.상태 = "Started!"
      }
    } else {
      게임방들.add(
        Lounge(
          최소_레벨 = 플레이어.레벨 - 10,
          최대_레벨 = 플레이어.레벨 + 10,
          플레이어들 = mutableListOf(플레이어),
          상태 = if (정원 == 1) "Started!" else "Waiting!"
        )
      )
    }
  }

  게임방들.forEach { 게임방 ->
    println(게임방.상태)
    게임방.플레이어들.sortedBy { it.닉네임 }.forEach { 플레이어 ->
      println("${플레이어.레벨} ${플레이어.닉네임}")
    }
  }
}