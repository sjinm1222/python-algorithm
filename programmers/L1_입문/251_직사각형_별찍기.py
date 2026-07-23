# 직사각형 별찍기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12969
# 알고리즘: 반복문
# 작성자: 학생
# 작성일: 2026. 07. 23. 13:50:46

a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*"*a)
