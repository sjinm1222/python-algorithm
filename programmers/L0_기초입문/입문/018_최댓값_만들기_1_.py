# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 05. 17:32:47

def solution(numbers):
    a=[]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                a.append(numbers[i]*numbers[j])
    return max(a)