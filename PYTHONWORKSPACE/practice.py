'''
# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 자료형
print('풍선')
print("나비")
print('ㅋㅋㅋ')
print('ㅋ'*9)

#boolean 자료형
#참/거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))

# 변수
# 애완동물을 소개해 주세요
animal = '고양이'
name = '나비'
age = 5
hobby = '낮잠'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '이에요')
print(name,'는 ',age,'살이며, ',hobby,'을 아주 좋아해요')
print(name + '는 어른일까요? ' + str(is_adult))


# Quiz) 변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station
# 변수값 : '사당', '신도림', '인천공항' 순서대로 입력
# 출력문장 : XX행 열차가 들어오고 있습니다
station = '사당'
print(station + '행 열차가 들어오고 있습니다')
station = '신도림'
print(station + '행 열차가 들어오고 있습니다')
station = '인천공항'
print(station + '행 열차가 들어오고 있습니다')


# 연산자-1
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)
print(5%3)
print(10%3)
print(5//3) #몫
print(10//3)

print(10>3)
print(4>=7)
print(10<3)
print(5<=5)

print(3==3)
print(4==2)
print(3+4 == 7)


# 연산자-2
print(1 != 3) # != 같지않다
print(not (1 != 3))

print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #True

print((3 > 0) or (2 > 4)) #True
print((3 > 0) | (2 > 4)) #True

print((5 > 4 > 3)) #T
print((5 > 4 > 7)) #F


#간단한수식
print(2+3*4) #14
print((2+3) *4) #20
number = 2+3*4 #14
print(number)
number = number+2 #16
print(number)
number += 2 #18
print(number)
number *= 2 #36
print(number)
number /= 2 #18
print(number)
number -= 2 #16
print(number)
number %= 5 #1
print(number)

#숫자처리함수
#abs 절대값 / pow 제곱 / round 반올림
print(abs(-5)) #abs 절대값 -> 5로 출력
print(pow(4, 2)) #4^2 = 4*4 = 16
print(max(5,12)) #12
print(min(5,12)) #5
print(round(3.14)) #3
print(round(4.99)) #5

from math import *
print(floor(4.99)) #내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근 4

#랜덤함수
from random import *

print(random()) #난수생성, 0.0 ~ 1.0미만의 임의의값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의값생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의값생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의값생성

print(int (random() *46)) #0~46미만 난수생성
print(int (random() *46) + 5) #5~51미만 난수생성


#로또만들기
from random import *
print(int(random()*45) +1) # 1~45 이하의 임의값생성
print(randrange(1,46)) # 1~46미만의 임의값 생성
print(randint(1,45)) # 1~45이하의 임의값 생성

#퀴즈 46:30
random = randint(4,28)
print('오프라인 스터디 모임 날짜는 매월 '+str(random)+' 일로 선정되었습니다')

#문자열
sentence ='나는 소년입니다'
print(sentence)
sentence2 ="파이썬은 쉬워요"
print(sentence2)
sentence3 ="""
나는 소년이고 
파이썬은 쉬워요
"""
print(sentence3)  # """ 3개쓰면 줄바꿈!

jumin = "990120-1234567"
print('성별 : ' + jumin[7])
print('연 : ' + jumin[0:2]) # 0부터 2앞까지
print('월 : ' + jumin[2:4])
print('일 : ' + jumin[4:6])

print('생년월일 : ' + jumin[0:6])
print('뒤 7자리 : ' + jumin[7:]) # 7부터 끝까지

print('뒤 7자리(뒤에서부터) : ' + jumin[-7:]) # 맨뒤에서 7번째부터 끝까지

#문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # lower 소문자
print(python.upper()) # upper 대문자
print(python[0].isupper()) # isupper 첫번째가 대문자이니?
print(len(python)) # len 길이를 반환
print(python.replace("Python", "Java")) #replace 문자대체

index = python.index('n')
print(index)
index = python.index('n', index+1) #두번째 n 찾기
print(index)

print(python.find('n')) # 5
print(python.find('Java')) #원하는 값이없으면 -1로 반환
#print(python.index('Java')) #index에 Java가 없으면 에러내고 끝낸다
# find와 index의 차이점 
# : find은 찾는값없으면 -1, index는 에러 ->종료

print(python.count('n')) # n이 몇번 찍히는지 카운트

#문자열 포맷
print("a"+"b")
print("a","b")

   #방법1
   # %d :정수,  %s :문자열,스트링, %c :문자, %s 전부다가능
print('나는 %d살입니다.' % 20) 
print('나는 %s을 좋아해요.' % "파이썬")
print('Apple은 %c로 시작해요.' %"A")

print('나는 %s살입니다.' % 20) 
print('나는 %s색과 %s색을 좋아해요.' % ("파란", "빨간")) 
print()
   #방법2
   # .format을 사용하면 형식상관없이 출력된다
print("나는 {}살입니다" .format(20))
print('나는 {}색과 {}색을 좋아해요.' .format("파란", "빨간")) 
print('나는 {0}색과 {1}색을 좋아해요.' .format("파란", "빨간")) 
print('나는 {1}색과 {0}색을 좋아해요.' .format("파란", "빨간")) 
print()
   #방법3
   # 변수처럼 이름을 줄 수 있다
print("나는 {age}이며, {color}색을 좋아해요." .format(age=20, color="빨간"))
print("나는 {color}이며, {age}색을 좋아해요." .format(age=20, color="빨간"))
print()
   #방법4 (v3.6 이상~)
   # 변수만들고, 출력 문자열 앞에 f를 쓴다
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출문자
# \n : 줄바꿈
print('백문이 불여일견 \n백견이 불여일타')
# \'  \"  : 문장 내에서 따옴표
print('저는 "나도코딩"입니다.')
print("저는 \"나노코딩\"입니다.")
# \\ : 문장 내에서 \
print("C:\\Users\\김재라\\Desktop\\PYTHONWORKSPACE>")
# \r : 커서를 맨 앞으로 이동 해서 덮어씌움
print("Red Apple\rPine")
# \b : 백스페이스 (한글자 삭제)
print("REdd\bApple")
# \t : 탭
print("Red\tApple")

#퀴즈
#url = "http://naver.com"
#url = "http://google.com"
url = "http://youtube.com"

my_str = url.replace("http://", "")
# my_str = my_str.replace(".com", "")
my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0~5직전까지(0,1,2,3,4)

password = my_str[:3]+str(len(my_str))+str(my_str.count('e'))+"!"
print("{0}의 비밀번호는 {1} 입니다 " .format(url, password))

#리스트[]

#지하철 칸별로 10명, 20명, 30명
#subway1 = 10
#subway2 = 20
#subway3 = 30

subway = [10,20,30]
print(subway)

subway =["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

#하하씨가 다음 정류장에 다음 칸에 탐
subway.append("하하")         #append 더하다 라는 뜻
print(subway)

#정형돈씨를 유재석/조세호 사이에 태워좀
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())     #pop 뒤에있는 사람 꺼냄
print(subway)

#같은 이름의 사람이 몇명 있는지 확인
subway.append("유재석")         #append 더하다 라는 뜻
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
#print(mix_list)

num_list.extend(mix_list)
print(num_list)
'''
