#%% 실수의 오류
'''
print(0.1+0.2)

print(0.1+0.2==0.3)

#&& 실수의 오류 해결방법! (1)
# 입력한 실수의 값들을 참인지 거짓인지 정확한 비교를 하고싶을때는 
# 외부에서 import를 가져온후 math라는 파일을 가져온다!
# is close 함수는 입력한 값의 근접한 값을 구하여 비교해주는 함수이다.
from ast import Num
import math

print(math.isclose(0.1+0.2, 0.3))

# 실수의 오류 해결방법! (2)

# 입력한 실수의 값들을 연산하여 정확한 결과값을 출력하고싶을때는 decimal을 사용한다!
from decimal import Decimal

print(float(Decimal('0.1')+ Decimal('0.2')))


#%% 퀴즈게임
#(삼항연산자로 사용가능)
qmsg = '다음 중 프로그래밍 언어가 아닌 것은?'
choiceMsg = '1.JAVA\n2.파이썬\n3.C언어\n4.망둥어\n'
choice=int(input(qmsg + '\n' + choiceMsg))
answer = 4

result=(('정답입니다!'if choice==answer else
         "오답..." if choice>=1 and choice <=4 else
          "잘못입력하셨습니다"))

# 가독성이 떨어진다!!!
print(result)

# 연산과 연결
print(10 + 9)       #19
print('10'+'9')     #'10'+'9' -> '109'
'''

#&& 
#----------------------------------------------------------------------------------
# 리스트 생성

numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('numbers =',numbers)

# 시퀀스 자료형(list, tuple, str 등) 값의 길이(length)
# → 시퀀스 자료형 값에 포함되어 있는 요소들(items)의 개수
# → len 함수를 이용해 시퀀스 자료형 값의 길이를 구할 수있다.

print('length of numbers =',len(numbers))

# 리스트 numbers에서 마지막 요소의 인덱스는 (length - 1)이다.
# 왜냐하면 인덱스는 0부터 시작하기때문이다.
print('numbers[9] =',numbers[9])        # 10

# 인덱스를 음수로 주면, 리스트의 마지막에서부터 위치를 계산한다.
print('numbers[-1] = ',numbers[-1])     # 10
print()

#--------------------------------------------------------------------------------------

#&&
# 시퀀스 자료형(sequence type)의 값의 슬라이스(slice) 연산
# → 시퀀스 자료형 값에서 일부분을 잘라낸 값들, 즉 부분 집합을 구하는 연산
# → range 함수와 매우 유사함.
# → 첫번째 인덱스(x)를 생략하면 기본 값은 0이 되고,
# → 두번째 인덱스(y)를 생략하면 기본 값은 시퀀스 자료형 값의 길이가(length)가 되고
# → 증가폭(step)을 생략하면 기본값은 1이 된다.

# range(x,y)
# → x <= n < y 범위에 포함된 정수들을 생성

# numbers[x : y]
# → 인덱스가 x <= n < y 범위에 포함된 부분 집합을 생성하라!

# numbers[2 : 6]
# → 인덱스가 2<= n <6 범위에 포함된 부분 집합을 생성하라!
# → 리스트의 numbers에서
# → 인덱스가 2 , 3, 4, 5 에 해당하는 요소들로 새로운 리스트를 생성하라!
# → [3, 4, 5, 6] 을 출력

print('numbers[2:6] = ',numbers[2:6])           # 3, 4, 5, 6

# numbers[:y]
# → numbers[0:y]
# → 리스트의 numbers에서
# → 인덱스가 0 <= n < y 범위에 포함된 부분 집합을 생성
# → 슬라이스 연산에서 첫번째 인덱스를 생략하면, 시퀀스 자료형 값의 처음을
#   시작위치로 설정  즉, 첫번째 인덱스는 첫번째 요소의 인덱스(0)이 된다.

# numbers[:4]
# → numbers[0:4]와 같은말
# → 리스트의 numbers에 인덱스가 0 <= n < 4 범위에 해당되는 부분집합을 생성!
# → 인덱스가 0, 1, 2, 3에 해당하는 요소들로 새로운 리스트를 생성
# → [1, 2, 3, 4] 를 출력

print('numbers[:4]',numbers[:4])        # 1, 2, 3, 4

# numbers[x:]
# → numbers[x : len(numbers)]와 같음
# → numbers[x : 10]
# → 리스트의 numbers에서 인덱스가 x <= n < 10 범위에 포함된 부분집합을 생성!
# → 슬라이스 연산에서 두번 째 인덱스를 생략하면, 시퀀스 자료형 값의 마지막을
# → 끝 위치로 설정 즉, 두번째 인덱스는 시퀀스 자료형값의 길이와 같다. = len(number)


# numbers[7:]
# → numbers[7:len(numbers)]
# → 리스트 numbers에서 인덱스가 7 <= n < 10 범위에 포함된 부분집합을 생성
# → 즉 인덱스가 7, 8, 9에 해당하는 요소들로 새로운 리스트를 생성
# → {8, 9, 10}을 출력

print('numbers[7:]',numbers[7:])        # 8, 9, 10

# range(x, y , step)
# → x <= n < y 범위에서 step 만큼 변하는 정수들을 생성
# → if step >0, then x <= n < y
# → if step <0, then x >= n < y


# numbers[x:y:step]
# → 리스트 numbers에서 인덱스가 x <= n < y 범위에 포함된 요소들 중에서, 
# → 인덱스가 x에서부터 step 만큼 변하는 요소들로 새로운 리스트를 생성
# → if step >0, then x <= n < y
# → if step <0, then x >= n < y


# numbers[3:8:2]
# → 리스트 numbers에서 인덱스가 3 <= n < 8 인덱스 범위 내에서 step이 2만큼씩 증가하는 
#   요소들로 새로운 리스트를 생성
# → 인덱스 요소가 3, 5, 7인 요소들로 새로운 리스트를 생성
# → {4, 6, 8}을 출력

print('numbers[3:8:2] = ',numbers[3:8:2])           # 4, 6, 8


# numbers[: : 3]
# → numbers[0:len(numbers):3]
# → numbers[0 : 10 :3]
# → 리스트 numbers에서 인덱스가 0 <= n < 9 인덱스 범위내에서 step이 3만큼씩 증가하는
#   요소들로 새로운 리스트를 생성!!
# → 인덱스 요소가 0, 3, 6, 9인 요소들로 새로운 리스트를 생성
# → [1, 4, 5, 7, 10] 을 출력

print('numbers[::3]',numbers[::3])      # 1, 4, 7, 10



#%% Q1. 튜플 numbers에서 짝수번째 요소들만 출력

# 튜플(tuple) 생성
# 값 변경 x
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

# 튜플 numbers의 짝수 번째 요소들
# → 튜플 numbers에서 인덱스가 1, 3, 5, 7, 9, 11인 요소들
# → 튜플 numbers에서 인덱스가 1<= n < 12 범위에 포함된 요소들 중에서,
#   인덱스가 1에서부터 2씩 증가하는 요소들

# → numbers[1:12:2]
# → numbers[1::2]

print(numbers[1: :2])



# %%
# Q2. 리스트 year와 poluation에서 일곰 번째에서부터 아홉번째 요소까지 추출

year = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892, 9783129]

print(year[6:])
print(population[6:])

# 리스트 year와 population에서 마지막 요소 3개를 추출
# → 인덱스가 6(-3), 7(-2), 8(-1)
# → 인덱스가 -3 <= n < -1 범위에 포함되는 요소들
# → 인덱스가 -3 <= n < 9 범위에 포함되는 요소들과 같다!!
# → year[-3:9]
# → year[-3:]

print(year[-3:])
print(population[-3:])
