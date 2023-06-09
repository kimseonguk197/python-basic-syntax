#0.함수란 무엇인가? (추후 배울 내용이므로 참고만)
#프로그램속 작은 프로그램, 많은 기본 프로그램이 파이썬에 내장되어 있고, 그것을 내장함수라고 부르고, 가끔은 library라고 표현하기도 한다.
# 아래 코드의 list(문자열)은 문자열을 잘라 list로 변환한것. 내장함수부터 수업후에 customizing함수 수업
a = "hobby"
def countCharacter(character):
    count = 0
    characterList = list(character)
    for c in characterList:
        if(c == 'b'):
           count = count +1
    return count
print(countCharacter(a))

#1.문자열 개수 세기 (함수활용)
a = "hobby"
countNum = a.count('b')
print(countNum)


#2.문자열 위치 확인하기 (함수활용)
a = "hobby"
findNum = a.find('o')
print(findNum)
# 문자열 길이 출력
print(len(a))

#2-1.찾았을때 없을 경구 -1 return
a = "hobby"
findNum = a.find('x')
print(findNum)


#4.소문자 <> 대문자 변경
a = 'hi'
print(a.upper())
a = 'HI'
print(a.lower())

#5.양쪽공백 지우기
a = ' hi pyhon '
print(a.strip())

#6.문자열 바꾸기
a = 'I studied python'
print(a.replace('python', 'java'))

#7.문자열 나누기
#공백으로 나누기
a = 'I studied python'
b = a.split()
print(b)

#특정문자열로 나누기
a = 'I:studied:python'
b = a.split(':')
print(b)
