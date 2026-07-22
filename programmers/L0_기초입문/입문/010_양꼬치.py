# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 22. 11:02:14

def solution(n, k):
    price_n=n*12000
    price_k=k*2000
    if n//10 > 1:
        answer=price_n+(price_k-n//10*2000)
    else:
        answer=price_n+price_k
    return answer