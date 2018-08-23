"""
Title   함수 function
Author  kadragon
Date    2018.08.23
"""


def pure_print():
    print("매개변수가 없는 함수")


def int_print(anything_int):
    """
    매개 변수가 1개인 함수

    :param anything_int: 출력할 정수 하나
    """
    print("정수 %d" % anything_int)


def user_sum(sum_a, sum_b):
    """
    매개 변수가 2개이고, 반환 값이 있는 함수 / 값 2개를 받아 돌려주는 함수
    Python 에서 함수는 언제나 값을 반환한다.
    명시되어 있지 않다면, None 객체를 명시되어 있다면 명시된 값을..

    :param sum_a: 값을 더할 1개의 정수
    :param sum_b: 값을 더할 또 다른 1개의 정수
    :return: 입력 받은 두개의 정수를 반환함
    """
    return sum_a + sum_b


def progression(n, step=1):
    """
    사용자가 입력한 값까지 증가하며 출력하는 함수
    매개변수(인수)의 디폴트 값을 설정할 수 있다.
    단, progression(step=1, n) 과 같이
    기본값을 갖는 인수 뒤에 기본값이 없는 인수가 존재 할 수 없다.

    :param n: 목적 정수
    :param step: 증가 단위 / 기본은 1
    """
    x = 1
    while x <= n:
        print(x, end=' ')
        x += step


progression(5)     # 출력: 1 2 3 4 5
print()
progression(10, 2)  # 출력: 1 3 5 7 9


def k_date_print(year, month, day):
    print("오늘은 %04d년 %02d월 %02d일 입니다." % (year, month, day))


k_date_print(2018, 8, 23)                   # 일반적인 인수 전달
k_date_print(month=8, day=23, year=2018)    # 키워드 인수 전달 방식
