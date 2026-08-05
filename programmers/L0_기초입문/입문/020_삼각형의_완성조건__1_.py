# 삼각형의 완성조건 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 06. 08:36:28

def solution(sides):
    a=sorted(sides,reverse=True)
    answer= 2 if a[0]>=a[1]+a[2] else 1
    return answer