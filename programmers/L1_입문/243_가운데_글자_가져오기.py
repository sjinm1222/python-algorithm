# 가운데 글자 가져오기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 알고리즘: 문자열
# 작성자: 학생
# 작성일: 2026. 07. 23. 13:46:03

def solution(s):
    if len(s) % 2 ==0:
        return s[int((len(s))/2-1)]+s[int(len(s)/2)]
    else:
        return s[int((len(s)-1)/2)]