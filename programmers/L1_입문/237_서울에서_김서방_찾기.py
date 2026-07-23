# 서울에서 김서방 찾기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12919
# 알고리즘: 배열, 탐색
# 작성자: 학생
# 작성일: 2026. 07. 23. 11:33:58

def solution(seoul):
    for i,s in enumerate(seoul):
        if s=="Kim":
            x=i
            break
    answer=f"김서방은 {x}에 있다"
    return answer