# 자릿수 더하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12931
# 알고리즘: 문자열, 반복문
# 작성자: 학생
# 작성일: 2026. 07. 23. 14:00:11

def solution(n):
    k=n
    answer=0
    while k > 0:
        a=k%10
        answer+=a
        k=k//10
    return answer