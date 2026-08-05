# 머쓱이보다 키 큰 사람
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 06. 08:22:18

def solution(array, height):
    a=0
    for i in array:
        if height < i:
            a+=1
    return a