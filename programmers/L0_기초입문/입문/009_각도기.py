# 각도기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 20. 13:55:25

def solution(angle):
    if angle < 90:
        answer=1
    elif angle  == 90:
        answer=2
    elif angle < 180:
        answer=3
    else:
        answer=4
    return answer