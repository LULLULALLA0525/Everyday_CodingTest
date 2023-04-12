# 코테 하면서 정리할 만한 꿀팁들

## **🔥itertools**

```python
from itertools import permutations
from itertools import combinations
from itertools import product
```

를 통해 import 할 수 있으며, 사용 방식은 다음과 같다.

</br>
</br>

### **1. 순열(permutations)**

```python
# permutations(<배열>, <고를 원소의 개수>)
test = ['A', 'B', 'C']
result = list(permutations(test, 2))
```

결과:
```python
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

</br>
</br>

### **2. 조합(combinations)**

```python
# combinations(<배열>, <고를 원소의 개수>)
test = ['A', 'B', 'C']
result = list(combinations(test, 2))
```

결과:
```python
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

</br>
</br>

### **3. 여러 리스트의 조합(product)**

```python
# product(*<이차원 배열>)
test = [['A', 'B'], ['가', '나'], ['1', '2']]
result = list(product(*test))
```

결과:
```python
[('A', '가', '1'),
 ('A', '가', '2'),
 ('A', '나', '1'),
 ('A', '나', '2'),
 ('B', '가', '1'),
 ('B', '가', '2'),
 ('B', '나', '1'),
 ('B', '나', '2')]
```

---

## **🔥리스트에서 중복 제거하기**

</br>

### **1. 집합(set)을 이용하여 중복 제거**

</br>

집합(set) 자료형은 중복이 불가능하다는 조건이 있기 때문에 리스트를 집합으로 바꾸고, 다시 리스트로 바꾸면 중복이 사라진다.</br>
단, 리스트가 오름차순으로 정렬되게 된다.

```python
arr = [6, 5, 6, 4, 4, 1, 1, 2, 3, 9, 8, 7, 9, 8, 7]
result1 = set(arr)
result2 = list(result1)
```

결과:

```python
result1 --> {1, 2, 3, 4, 5, 6, 7, 8, 9}
result2 --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

</br>

### **2. for 문을 이용하여 중복 제거**

</br>

집합(set)을 통해 중복을 제거하며 정렬되는 것이 싫다면 for 문을 통해서도 중복을 제거할 수 있다.

```python
arr = [6, 5, 6, 4, 4, 1, 1, 2, 3, 9, 8, 7, 9, 8, 7]
result = []  #중복을 제거한 리스트를 저장할 리스트

for elem in arr:
    if elem not in result1:
        result.append(elem)
```

결과:

```python
result --> [6, 5, 4, 1, 2, 3, 9, 8, 7]
```

---

## **🔥자료구조 - 스택(STACK)**

</br>

스택은 별도의 import 없이 List를 활용해서도 사용할 수 있으며, 사용 방식은 다음과 같다.

</br>
</br>

```python
stack = []          #스택 초기화

stack.append(1)     #스택에 요소 넣기
a = stack.pop()     #스택의 오른쪽(가장 나중에 들어간 요소)에서 요소 꺼내기
```

---

## **🔥자료구조 - 큐(QUEUE)**

</br>

```python
from collections import deque
```

를 통해 import 할 수 있으며, 사용 방식은 다음과 같다.

</br>
</br>

```python
queue = deque()         #큐 초기화

queue.append(1)         #큐에 요소 넣기
a = queue.popleft()     #큐의 왼쪽(가장 먼저 들어간 요소)에서 요소 꺼내기
queue.appendleft()      #큐의 왼쪽에 요소 넣기

queue.reverse()         #큐에 저장된 요소 순서 뒤집기
```

---

## **🔥리스트를 정렬하는 다양한 방법**

</br>

리스트를 정렬하는 데에는 다양한 방법이 있다.

```python
a = [3, 4, 1, 9, 5, 6, 2, 7, 8]
b = sorted(a)	# [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = a.sort()	# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

</br>

위 방법은 단순히 값에 따라서 오름차순으로 정렬할 때 사용할 수 있지만,
다양한 옵션값을 넣어서 정렬할 수도 있다.

```python
a = [3, 4, 1, 9, 5, 6, 2, 7, 8]
b = sorted(a, reverse=True)		# [9, 8, 7, 6, 5, 4, 3, 2, 1], 내림차순
```

```python
a = [["carrot", 1], ["apple", 3], ["banana", 5], ["peanut", 3]]
# 이름([0]) 순으로 정렬
b = sorted(a, key=lambda x: x[0])
# [["apple", 3], ["banana", 5], ["carrot", 1], ["peanut", 3]]

# 당도([1]) 역 순으로 정렬
c = sorted(a, key=lambda x: -x[1])
# [["banana", 5], ["apple", 3], ["peanut", 3], ["carrot", 1]]

# 당도([1]) 순으로 정렬하며, 같은 값이 있을 경우에는 이름([0]) 순으로 정렬
d = sorted(a, key=lambda x:(-x[1], x[0]))
# [["banana", 5], ["apple", 3], ["peanut", 3], ["carrot", 1]]
```

---

## **🔥문자열 사이에 다른 문자열을 삽입하는 방법**

</br>

간단하게 슬라이싱을 활용하여 문자열 사이에 다른 문자열을 삽입할 수 있다.

```python
s = "abdefg"
res = s[:2] + 'c' + s[2:]
```

---

## **🔥조금 더 빠른 입출력**

</br>

일반적인 python 입출력으로는 애매하게 시간 초과가 나는 경우가 있다. 그럴 경우에는 다음과 같은 입출력 방법을 사용해보자.

```python
import sys
input = sys.stdin.readline
print = sys.stdout.write
```

위에 얘네들만 추가해주면 자동으로 input()이나 print()만 써도 된다.</br>
대신 print() 내부에는 string만 넣어야 한다.

---

## **🔥BFS와 DFS**

</br>

맨날 까먹는 BFS와 DFS. 그냥 적어두자.

### **- BFS**

```python
def bfs(graph, start):
    result = []
    visited = [False] * (N + 1)
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        if not visited[cur]:
            visited[cur] = True
            [...]
            for nxt in graph[cur]:
                if not visited[nxt]:
                    queue.append(nxt)
```
너가 알고 있는 그 **Queue**쓰는 알고리즘이 바로 BFS다.</br>
Queue에 있는 것들을 하나씩 꺼내면서 그 주변 모든 것들을 Queue의 맨 뒤에 넣고, 그대로 반복</br>
상황에 따라 중복처리나 조건처리를 해주면 된다.</br>
[...] 있는 곳에 순회하면서 수행할 작업을 넣으면 된다.
넣으면서 수행하는 방법도 있고, 빼면서 수행하는 방법도 있는데, 위 코드는 전자다.

<br><br>

### **- DFS**

```python
def dfs(graph, dfs_visited, start):
    dfs_visited[start] = True
    [...]
    for nxt in graph[start]:
        if not dfs_visited[nxt]:
            dfs(graph, dfs_visited, nxt)
```

DFS가 더 쉽다. 쫄지마라.<br>
BFS는 Queue가 마를 때까지 도는 거라면, BFS는 **재귀함수**다.<br>
대신 재귀가 끝나는 타이밍이 있어야 하므로 visited 배열을 활용해준다.<br>
[...] 있는 곳에 순회하면서 수행할 작업을 넣으면 된다.