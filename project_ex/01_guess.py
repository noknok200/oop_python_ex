"""
Title       숫자 알아 맞히기 게임
Reference   나만의 Python Game 만들기 Chapter 4 p.53
Author      kadragon
Date        2018.08.21
"""

# Generate pseudo-random numbers
import random       # random 모듈을 사용하겠다고 선언. C 언어의 include 와 비슷

guessesTaken = 0    # 사용자가 추측한 횟수를 저장하기 위해 사용하는 변수
guess = 0           # 사용자가 추측한 숫자를 저장

# https://docs.python.org/ko/3/library/functions.html#input
myName = input('Hello! What is your name: ')    # python3 에서 input()은 문자열을 반환한다.

# https://docs.python.org/ko/3/library/random.html#random.randint
number = random.randint(1, 20)  # 1 ~ 20 (include 1, 20) 임의의 정수를 가져오는 module 을 활용
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # 문자열을 연결할 때 '+' 연산자를 활용할 수 있다.

while guessesTaken < 6:
    print('Take a guess.')
    guess = int(input())  # 문자열을 반환하기 때문에 int() 내장 함수를 이용하여 정수로 변환한다.

    guessesTaken += 1

    if guess == number:  # 맞췄으니 게임을 종료한다.
        break
    else:
        print('Your guess is too ' + ('low.' if guess < number else 'high'))  # if 를 활용한 한줄 코딩 방식이다. 익숙해지자.

if guess == number:
    print('Good job, %s! You guessed my number in %d guesses!' % (myName, guessesTaken))

elif guess != number:
    print('Nope. The number I was thinking of was %d' % number)
