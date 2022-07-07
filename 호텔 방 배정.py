
def solution(k, room_number):
    result = []
    
    START, END = 0, 1
    empty_room = [[1, k]]
    
    for query in room_number:
        prev_room = 0;
        for index in range(len(empty_room)):
            print(f"query: {query}, index: {index}, empty_room: [{empty_room[index][START]}, {empty_room[index][END]}]")
            if query >= empty_room[index][START] and query <= empty_room[index][END]:   # 방이 비어있음
                
                result.append(query)
                
                if empty_room[index][START] == empty_room[index][END]:
                    empty_room.pop(index)
                elif query == empty_room[index][START]:
                    empty_room[index] = [query + 1, empty_room[index][END]]
                elif query == empty_room[index][END]:
                    empty_room[index] = [empty_room[index][START], query - 1]
                else:
                    empty_room.append([query + 1, empty_room[index][END]])
                    empty_room[index] = [empty_room[index][START], query - 1]
                    
            elif query > prev_room and query < empty_room[index][START]:                # 요청한 방이 차 있음
                
                result.append(empty_room[index][START])
                
                empty_room.pop(index)
            
            else:                                                                       # 그 외에는 패스
                prev_room = empty_room[index][END]
                continue
    
    return result

k = int(input())
# 10
room_number = list(map(int, input().split()))
# 1 3 4 1 3 1

print(solution(k, room_number))
# 1 3 4 2 5 6