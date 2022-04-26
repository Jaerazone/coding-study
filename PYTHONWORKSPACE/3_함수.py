'''
#함수
def open_account():
    print("새로운 계좌가 생성 되었습니다")
    
open_account()

def deposit(balance, money): #입금하는 함수
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다" .format(balance+money))
    return balance+money

def withdraw(balance, money):#출금하는 함수
    if balance>money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다" .format(balance-money))
        return balance-money
    else:
        print("잔액이 충분하지 않습니다. 잔액은 {0} 원입니다" .format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금 수수료발생
    commission = 100 #수수료 100원
    return commission, balance-money-commission #튜플형식

balance = 0 #잔액
balance = deposit(balance, 2000)
balance = withdraw(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}입니다" .format(commission, balance))
print(balance)

#기본값 같이 설정하는 함수
def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")
#같은 학교 같은 학년 같은반 같은 수업
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
        .format(name, age, main_lang))
profile("유재석")
profile("김태호")

#키워드 함수(순서대로 호출)
def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

#가변인자를 이용한 함수 호출 (가변인자는 *로 시작함)
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
    
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "JKotlin", "Swift")


#지역변수 와 전역변수
gun =10
def checkpoint(soldiers): #경계근무
    global gun #전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))

def checkpoint_ret(gun,soldiers):
    gun = gun-soldiers
    print("[함수내 ] 남은총 : {0}".format(gun))
    return gun

print("전체 총 : {0}" .format(gun))
# checkpoint(2) #2명이 경계 근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}" .format(gun))

#퀴즈

def std_weight(height, gender):
    if(gender == "남자"):
        return height * height * 22
    elif(gender =="여자"):
        return height * height * 21
    
height = 175
gender = "남자"
weight = round(std_weight(height*0.01, gender), 2) #소수점2번째까지만 출력, 반올림해주는듯
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다." .format(height, gender, weight))

#표준입출력
print("Python", "Java", "Javascript", sep=" vs ") #sep : 단어사이 ' vs ' 해준다
print("Python", "Java", sep=",", end="?")  #end : 문장의 끝부분을 '?'로 해주고, 밑문장 연달아서 붙임
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

#시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): #items를쓰면 key와 value 둘다들고옴
    #print(subject, score)
    print(subject.ljust(8) , str(score).rjust(4), sep=":")

#은행 대기순번표
# 001, 002, 003, ...
for num in range(1,21):
    print("대기번호 : "+str(num).zfill(3))
 
answer = input("아무값이나 입력하세요 : ") #숫자든 문자든 input으로 입력받으면 항상 string 문자형으로 값저장됨!!
print(type(answer))
print("입력하신 값은 " + answer + "입니다")

#다양한 출력 포맷
#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
print("{0: >10}".format(+500)) # 양수 +기호 표시 안됨
print("{0: >10}".format(-500))
#양수일땐 +로 표시, 음수일땐 -로 표시
print("{0: >+10}".format(500)) # 양수 +표시된다!!
print("{0: >+10}".format(-500))
print()
#왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(500))
print("{0:_<+10}".format(500))
#3자리 마다 콤마 찍어주기
print("{0:,}".format(100000000000))
#3자리 마다 콤마 찍어주기, +=부호도 넣기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))
#3자리 마다 콤마 찍어주기, 부호도 붙이고, 자리수 확보하기
# 돈이 많으면 행복하지 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(100000000000))
#소수점 출력
print("{0:f}".format(5/3))
#소수점 특정 자리수까지만 표시 (소수점 3째 자리에서 반올림, 2자리까지 나옴)
print("{0:.2f}".format(5/3))
  
#파일 입출력
score_file = open("score.txt", "w", encoding="utf8") #"w" write의목적으로쓸거다, utf8 한글쓸때 필수
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") #이 줄 반복하면 덮어씌워지기때문에, "a" : 이어쓰기를 적어줌
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # "r"은 파일 읽어오기
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # "r"은 파일 읽어오기
print(score_file.readline(), end="") #줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
print(score_file.readline(), end="") # , end="" 줄바꿈싫어서 써줌
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
''' 
#파일의 줄이 엄청 길때. while 반복문으로 읽어온다
score_file = open("score.txt", "r", encoding="utf8") # "r"은 파일 읽어오기
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()