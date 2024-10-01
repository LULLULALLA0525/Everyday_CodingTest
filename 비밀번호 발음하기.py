import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(password):
  vowels = 'aeiou'
  isVowel = [char in vowels for char in password]

  if not any(isVowel):
    return '<'+password+'> is not acceptable.'
  
  for i in range(2, len(password)):
    if isVowel[i - 2] == isVowel[i - 1] and isVowel[i - 1] == isVowel[i]:
      return '<'+password+'> is not acceptable.'
    
  for i in range(1, len(password)):
    if password[i - 1] == password[i]:
      if password[i] != 'e' and password[i] != 'o':
        return '<'+password+'> is not acceptable.'
      
  return '<'+password+'> is acceptable.'

ANSWERS = []
while True:
  PASSWORD = input()
  if PASSWORD == 'end':
    break
  ANSWERS.append(solution(PASSWORD))

for ANSWER in ANSWERS:
  print(ANSWER)