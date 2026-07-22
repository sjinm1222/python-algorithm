# 짝수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 22. 14:55:18

def solution(n):
    k=[i for i in range(1,n+1) if i % 2 ==0]
    answer=sum(k)
    return answer