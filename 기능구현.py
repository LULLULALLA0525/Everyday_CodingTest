def daysToFinish(progress: int, speed: int) -> int:
    remain = 100 - progress
    days = remain // speed
    if remain % speed != 0:
        days += 1
    return days

def solution(progresses, speeds):
    answer = []
    
    days = [0 for _ in range(len(progresses))]
    for i in range(len(days)):
        days[i] = daysToFinish(progresses[i], speeds[i])
    
    cnt = 0
    first_publish = 0
    for d in days:
        if cnt == 0:
            first_publish = d
            
        if d <= first_publish:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            first_publish = d
            
    if cnt != 0:
        answer.append(cnt)
    
    return answer