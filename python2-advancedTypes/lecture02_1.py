# # 변수는 변수명당 각각의 데이터를 담는다. 그러나 변수가 많아질수록 관리하기가 힘들기 때문에, 리스트 등장.

# a = "김돌쇠"
# b = "김갑돌"
# c = "김갑순"
# d = "김철수"
# print(d)

# #하나의 변수로 여러개의 데이터를 담고 관리.

# lista = ["김돌쇠", "김갑돌", "김갑순", "김철수"]
# print(lista)
# print(lista[0])

# #리스트 숫자
# lista = [1, 2, 3, 4]
# print(lista[0])

# #리스트 숫자+문자
# lista = [1, 2, "김돌쇠", "김갑돌"]
# print(lista[0])

# #리스트 리스트+숫자
# lista = [["김돌쇠", "김갑돌"], 1, 2]
# print(lista[0][0])

# #리스트의 슬라이싱 : 결과값은 list로
# lista =  ["김돌쇠", "김갑돌", "김갑순", "김철수"]
# print(lista[1:2])
# print(lista[:2])
# print(lista[2:])

# #리스트더하기
# lista =  ["김돌쇠", "김갑돌", "김갑순", "김철수"]
# listb = [1,2,3,4,5]
# listc = lista + listb
# print(listc)


# #리스트 반복하기
# lista =  ["김돌쇠", "김갑돌", "김갑순", "김철수"]
# listb = lista * 3;
# print(listb)

# #리스트값 수정하기 >> 1개값 바꿀땐 1개변수로, 여러값 바꿀떈 다른 리스트로 교체
# lista  = [ 1, 3, 5, 7, 9, 10]
# lista[2] = 4
# print(lista)
# lista  = [ 1, 3, 5, 7, 9, 10]
# lista[1:5] = [2,3,4,5]
# print(lista)

# #리스트 값 삭제하기 >> 빈리스트로 교체
# lista =  ["김돌쇠", "김갑돌", "김갑순", "김철수"]
# lista[0:1] =[]
# del lista[0:2]
# print(lista)
# lista[0:2] = []
# print(lista)
# # 인덱스가 아닌 값으로 삭제시
# lista.remove("김돌쇠")
# print(lista)

# # 리스트에 요소추가 >> append >>맨뒤에 추가. 리턴값이 없는 함수라는 것도 특이점.(대상 변수를 직점 바꿈)
# # extend는 iterable한 객체(리스트, 튜플, 집합 등)의 모든 요소를 추가시 사용
# lista =  ["김돌쇠", "김갑돌", "김갑순", "김철수"]
# lista.append("안철수")
# lista.insert(2,"안철수")
# lista.extend(["박돌쇠", "박갑돌"])
# print(lista)


#리스트 정렬 >> sort >> 숫자는 낮은숫자부터, 문자는 ㄱㄴㄷㄹ abcd 순으로 정렬. 리턴값 없음.(대상 변수를 직점 바꿈)
# lista =  ["김돌쇠", "김갑돌", "김갑순", "김철수"]
# lista.sort()
# print(lista)

#리스트 뒤집기 >> reverse >> 뒤에서부터 순서변경, 리턴값 없음.(대상 변수를 직점 바꿈)
# lista =  ["김돌쇠", "김갑돌", "김갑순", "김철수"]
# lista.reverse()
# print(lista)

# # 리스트 뒤집기 >> reverse >> 뒤에서부터 순서변경, 리턴값 있음.(대상 변수를 직점 바꾸지 않음.)
# lista =  ["김돌쇠", "김갑돌", "김갑순", "김철수"]
# indexNum = lista.index("김철수")
# print(indexNum)
# stra = "Courage is very important. Like a muscle, it is strengthened by use."
# indexNum2 = stra.index("b")
# print(indexNum2)

# #리스트 요소 꺼내기 (pop) >> 마지막 요소 꺼내는 
# lista =  ["김돌쇠", "김갑돌", "김갑순", "김철수"]
# lista.pop()
# print(lista)

# lista =  ["김돌쇠", "김갑돌", "김갑순", "김철수"]
# countNum = lista.count("김돌쇠")
# print(countNum)


#제곱 문제풀이   x**y : x의 y제곱승
x=2
y = 2.5*(x**2) + 3.3*x + 6
print("2차 방정식 결과 = ", y)

#리스트 연습문제1  110p.
lst = [10, 1, 5,2]
result = lst * 2
print("단계 1", result)
result.append(lst[0]*2)
print("단계2 :", result)
result2 = result[1:len(result):2]
# result2 = result[1::2]
print("단계3 :", result2)