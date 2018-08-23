"""
Title   string 문자열 관련
Author  kadragon
Date    2018.08.23
"""
import sys

a = "Life is too short, You need Python"
print(type(a))      # 출력: <class 'str'>

# 0 부터 시작하는 인덱스를 이용하여 각각 접근 할 수 있다.
# a[0] = 'K' 단, 이렇게 개별 변경은 불가능 하다.
print(a[-1] + a[0])

print(a[0:4])       # 출력: Life

print(a[19:])       # 출력: You need Python
print(a[19:-7])     # 출력: You need

a = "Pithon"
print(a[:1] + 'y' + a[2:])  # 출력: Python

a = "hobby"
print(a.count('b'))     # 출력: 2

print(a.find('y'))      # 출력: 0, 찾는 값이 없으면 -1
print(a.index('y'))     # 출력: 0, find 와 동일하지만, 없으면 exception 에러

a = ','
print(a.join('abcd'))   # 출력: a,b,c,d


a = "  hi  "
print(a.strip())        # 출력: hi / a.lstrip() / a.rstrip()
print(a.strip() * 3)    # 출력: hihihi

a = "Life is too short"
print(a.replace("Life", "Your leg"))    # 출력: Your leg is too short