"""
Title       드래곤 왕국
Reference   나만의 Python Game 만들기 Chapter 6 p.87
Author      kadragon
Date        2018.08.21
"""

# Time access and conversions
import time
# Generate pseudo-random numbers
import random

"""
Python Enhance Proposal(PEP 8)
Style Guide for Python Code
    - 변수 및 함수를 정의 할때 이름에 uppercase(대문자) 를 사용하지 않는다.
    - 최상위(top-level) 함수와 클래스 정의는 2줄씩 띄어 쓴다.
    - 클래스 내의 메소드 정의는 1줄씩 띄어 쓴다.
"""

text_line = 80
sleep_time = 2


def display_intro():  # intro 함수 python 에서는 함수를 def 을 이용하여 정의한다. 반환형을 명시하지 않는다.
    print('=' * text_line)
    print("""
    You are in a land full of dragons. 
    In front of you, you see two caves. 
    In one cave, the dragon is friendly and will share his treasure with you. 
    The other dragon is greedy and hungry, and will eat you on sight.
    """)
    print('=' * text_line)


def choose_cave():  # 동굴을 선택하는 함수
    cave = ' '
    while cave != '1' and cave != '2':
        cave = input('Which cave will you go intro? (1 or 2): ')

    return cave


def check_cave(chosen_cave):  # 결과를 보여주는 함수
    print('You approach the cave...')
    """
    https://docs.python.org/ko/3/library/time.html#time.sleep
    sleep(seconds) 는 실수를 받아 그 시간만큼 실행을 지연시킨다.
    """
    time.sleep(sleep_time)
    print('It is dark and spooky...')
    time.sleep(sleep_time)
    print('A large dragon jumps out in front of you! He opens his jaws and...\n')
    time.sleep(sleep_time)

    friendly_cave = random.randint(1, 2)

    if chosen_cave == str(friendly_cave):  # random.randint 에 의해 나온 값은 정수이고, 사용자에게 받은 값은 문자형이기에 형태를 맞춰준다.
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')


play_again = 'yes'  # 플레이를 지속할지를 입력 받아 임시 저장하는 공간

while play_again == 'yes' or play_again == 'y':
    display_intro()

    cave_number = choose_cave()

    check_cave(cave_number)
    print('\n' + ('=' * text_line))
    play_again = input('Do you want to play again? (yes or no): ')
