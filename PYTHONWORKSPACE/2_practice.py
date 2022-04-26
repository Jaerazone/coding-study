
#사전자료 정수형
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) # 없는값을 부르면 오류남
print(cabinet.get(5)) #없는값이라도 get으로 부르면 None 출력하고 아래 hi 출력
print(cabinet.get(5,"사용가능")) # (key없으면, "기본값") 출력
print("hi")

print(3 in cabinet) #캐비넷에 3이 있으면 true, false 확인
print(5 in cabinet)

#사전자료 스트링형
cabinet ={"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print(cabinet.get("A-3"))

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)

#튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")  튜플은 추가가 안된다

# name="김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

name, age, hobby = "김종국", 20, "코딩"
print(name, age, hobby)

#세트( 집합, set )
#중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 (java와 python을 모두 할수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (java또는 python 할수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합 (java는 할수 있지만 python은 못하는 개발자)
print(java - python)
print(java.difference(python))

#python 할줄 아는 사람 늘어남
python.add("김태호")
print(python)

#java 를 까먹었어요
java.remove("김태호")
print(java)

#자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#퀴즈
from random import *
users = range(1,21)  #1부터 20까지
print(users, type(users))
users = list(users)
print(users, type(users))
# print(users)
# shuffle(users) # shuffle 무작위로 배열 바꿈
# print(users)
# print(sample(users,1)) # 배열중에 무작위로 1개만 출력
#shuffle(users)

#   내가 푼 방법

#   chi = sample(users,1)
#   users.remove(chi[0])
#   coffee = sample(users,3)

#   print(" -- 당첨자 발표 -- ")
#   print("치킨 당첨자 :" + str(chi[0]))
#   print("커피 당첨자 :" + str(coffee))
#   print(" -- 축하 합니다 -- ")


#선생님 답안
print(users)
shuffle(users) #무작위로 배열바꿈
print(users)
winners = sample(users,4) #4명중에서 1명은 치킨, 3명은 커피

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))
print(" -- 축하 합니다 -- ")

# if
weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather=="눈":
    print("우산을 챙기세요")
elif weather =="미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온이 어때요?"))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10<= temp and temp <30:
    print("괜찮은 날씨에요")
elif 0<=temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요")

# for in 반복문
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

for waiting_no in [0,1,2,3,4]: #0,1,2,3,4
    print("대기번호 : {0}" .format(waiting_no))

print()

for waiting_no in range(1,6): #1,2,3,4,5
    print("대기번호 : {0}" .format(waiting_no))

print()

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다" .format(customer))

# while 반복문
customer = "토르"
index = 5
while index >=1 :
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요" .format(customer, index))
    index -= 1
    if index ==0:
        print("커피는 폐기처분되었습니다")
        
#무한 루프에 빠짐
customer ="아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1}회" .format(customer, index))
    index += 1

customer = "토르"
person ="Unknown"

while person != customer : 
    print("{0}, 커피가 준비 되었습니다." .format(customer))
    person = input("이름이 어떻게 되세요?")
#while문은 조건이 맞을때까지 계속 반복
#조건맞으면 반복문 탈출~!

# continue, break 문
absent = [2,5] #결석
no_book = [7] # 책을 깜빡했음
for student in range(1,11): # 1~10 까지 학생
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지 {0}는 교무실로 따라와" .format(student))
        break
    print("{0}, 책 읽어봐" .format(student))
    #continue는 조건 맞으면 다음식 실행안하고, 반복문으로 다시올라감
    #break는 조건이 맞으면, 반복문 바로종료

# 출석번호 1,2,3,4 앞에 100을 붙이기로함 -> 101,102,103,104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)
#학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)
#학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

#퀴즈
from random import *

count = 0 # 탑승 승객수

# print(int (random() *46)) #0~46미만 난수생성
#time = print(int (random() *46) + 5) #5~51미만 난수생성

for i in range(1,51): #1~50 이라는 수
    time = randrange(5,51) #5~50분 사이 랜덤 소요시간
    if(5 <= time <= 15) :
        print("[O] {0}번째 손님 (소요시간 : {1}분) " .format(i,time))
        count +=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)" .format(i,time))
print("총 탑승 승객 : {0}분" .format(count))

