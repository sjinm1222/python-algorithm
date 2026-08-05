# 피자 나눠 먹기 (3)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 06. 08:40:33

def solution(slice, n):
    import math
    answer = math.ceil(n/slice)
    return answer